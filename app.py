from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, func
import os
import uuid
from datetime import datetime

# ======================
# APP
# ======================
app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "troque-esta-chave")

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=False
)

# ======================
# DATABASE
# ======================
database_url = os.getenv("DATABASE_URL")

if database_url:
    database_url = database_url.replace(
        "postgres://",
        "postgresql://"
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url

else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database_reduzido.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ======================
# MODELOS
# ======================
class Produto(db.Model):
    __tablename__ = "produto"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.Text, nullable=False)
    subcategoria = db.Column(db.Text)
    preco = db.Column(db.Float)
    imagem = db.Column(db.Text)
    descricao = db.Column(db.Text)
    link = db.Column(db.Text)
    destaque = db.Column(db.Integer, default=0)


class CliqueAfiliado(db.Model):
    __tablename__ = "cliques"

    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer)
    click_id = db.Column(db.String(100), unique=True)
    ip = db.Column(db.String(50))
    user_agent = db.Column(db.Text)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

# ======================
# UTIL
# ======================
def limpar(valor, padrao="Geral"):
    if valor is None:
        return padrao

    valor = str(valor).strip()

    if valor.lower() in ["none", "null", "", "others", "other"]:
        return padrao

    return valor[:40].title()

# ======================
# GRUPOS
# ======================
def criar_grupos(produtos):
    grupos = {}

    for p in produtos:
        if not p or not p.nome or not p.link:
            continue

        cat = limpar(p.categoria, "Outros")
        sub = limpar(p.subcategoria, "Geral")

        grupos.setdefault(cat, {})
        grupos[cat].setdefault(sub, [])
        grupos[cat][sub].append(p)

    return grupos

# ======================
# 🔥 RANKING POR CLIQUES
# ======================
def get_mais_clicados(limit=8):
    return db.session.query(
        Produto,
        func.count(CliqueAfiliado.id).label("total")
    ).join(CliqueAfiliado, Produto.id == CliqueAfiliado.produto_id)\
     .group_by(Produto.id)\
     .order_by(func.count(CliqueAfiliado.id).desc())\
     .limit(limit)\
     .all()

# ======================
# HOME (MELHORADA)
# ======================
@app.route("/")
def home():

    busca = request.args.get("q", "").strip()
    pagina = request.args.get("pagina", 1, type=int)

    query = Produto.query

    # 🔎 busca
    if busca:
        query = query.filter(
            or_(
                Produto.nome.ilike(f"%{busca}%"),
                Produto.categoria.ilike(f"%{busca}%"),
                Produto.subcategoria.ilike(f"%{busca}%")
            )
        )

    query = query.order_by(Produto.id.desc())

    paginacao = query.paginate(
        page=pagina,
        per_page=24,
        error_out=False
    )

    produtos = paginacao.items
    grupos = criar_grupos(produtos)

    # ======================
    # 🔥 RECOMENDADOS INTELIGENTES
    # ======================
    recomendados = []

    if pagina == 1 and not busca:

        # 1) produtos mais clicados (ranking real)
        clicados = get_mais_clicados(8)
        recomendados = [p[0] for p in clicados]

        # 2) fallback se não tiver dados
        if not recomendados:
            recomendados = Produto.query.filter_by(destaque=1)\
                .order_by(Produto.id.desc())\
                .limit(8)\
                .all()

        # 3) fallback final
        if not recomendados:
            recomendados = Produto.query.order_by(Produto.id.desc())\
                .limit(8)\
                .all()

    return render_template(
        "index.html",
        produtos=produtos,
        grupos=grupos,
        recomendados=recomendados,
        paginacao=paginacao,
        busca=busca
    )

# ======================
# AFILIADO (NÃO ALTERAR)
# ======================
@app.route("/go/<int:produto_id>")
def go(produto_id):

    produto = db.session.get(Produto, produto_id)

    if not produto or not produto.link:
        return redirect(url_for("home"))

    link = str(produto.link).strip()

    try:
        db.session.add(
            CliqueAfiliado(
                produto_id=produto.id,
                click_id=str(uuid.uuid4()),
                ip=request.remote_addr,
                user_agent=request.headers.get("User-Agent")
            )
        )
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        print("Erro clique:", e)

    return redirect(link, code=302)

# ======================
# CLIQUE AJAX
# ======================
@app.route("/clique", methods=["POST"])
def registrar_clique():

    data = request.get_json() or {}
    produto_id = data.get("produto_id")

    if not produto_id:
        return jsonify({"status": "invalid"})

    produto = db.session.get(Produto, produto_id)

    if not produto:
        return jsonify({"status": "not_found"})

    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent", "")

    try:
        existe = CliqueAfiliado.query.filter_by(
            produto_id=produto_id,
            ip=ip
        ).first()

        if not existe:
            db.session.add(
                CliqueAfiliado(
                    produto_id=produto_id,
                    click_id=str(uuid.uuid4()),
                    ip=ip,
                    user_agent=user_agent
                )
            )
            db.session.commit()

    except Exception as e:
        db.session.rollback()
        print("Erro clique:", e)

    return jsonify({"status": "ok"})

# ======================
# CATEGORIA
# ======================
@app.route("/categoria/<nome>")
def categoria(nome):

    pagina = request.args.get("pagina", 1, type=int)

    query = Produto.query.filter_by(categoria=nome)\
        .order_by(Produto.id.desc())

    paginacao = query.paginate(
        page=pagina,
        per_page=24,
        error_out=False
    )

    produtos = paginacao.items
    grupos = criar_grupos(produtos)

    return render_template(
        "index.html",
        produtos=produtos,
        grupos=grupos,
        paginacao=paginacao,
        busca=""
    )

# ======================
# LOGIN / ADMIN
# ======================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("user") == "admin" and request.form.get("senha") == "123":
            session["logado"] = True
            return redirect(url_for("admin"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/admin")
def admin():
    if session.get("logado") is not True:
        return redirect(url_for("login"))

    produtos = Produto.query.order_by(Produto.id.desc()).limit(200).all()
    return render_template("admin.html", produtos=produtos)

# ======================
# DASHBOARD
# ======================
@app.route("/dashboard")
def dashboard():
    if session.get("logado") is not True:
        return redirect(url_for("login"))

    dados = db.session.query(
        Produto.nome,
        func.count(CliqueAfiliado.id).label("total")
    ).join(CliqueAfiliado, Produto.id == CliqueAfiliado.produto_id)\
     .group_by(Produto.id, Produto.nome)\
     .order_by(func.count(CliqueAfiliado.id).desc())\
     .all()

    return render_template("dashboard.html", dados=dados)

# ======================
# START
# ======================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=5000)
