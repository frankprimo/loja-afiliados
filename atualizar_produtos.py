import pandas as pd
from app import app, db, Produto


ARQUIVO_CSV = "shopee.csv"


def atualizar():

    df = pd.read_csv(ARQUIVO_CSV)

    with app.app_context():

        for _, linha in df.iterrows():

            produto = Produto.query.filter_by(
                nome=linha["title"]
            ).first()

            if produto:

                produto.preco = linha["sale_price"]
                produto.imagem = linha["image_link"]
                produto.link = linha["product_link"]

            else:

                novo_produto = Produto(
                    nome=linha["title"],
                    preco=linha["sale_price"],
                    imagem=linha["image_link"],
                    descricao=linha.get("description", ""),
                    link=linha["product_link"]
                )

                db.session.add(novo_produto)


        db.session.commit()

    print("Produtos atualizados com sucesso!")


if __name__ == "__main__":
    atualizar()