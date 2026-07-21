import sqlite3
import os

BANCO_ORIGINAL = "database.db"
BANCO_REDUZIDO = "database_reduzido.db"

# Remove o banco reduzido antigo, se existir
if os.path.exists(BANCO_REDUZIDO):
    os.remove(BANCO_REDUZIDO)

origem = sqlite3.connect(BANCO_ORIGINAL)
destino = sqlite3.connect(BANCO_REDUZIDO)

co = origem.cursor()
cd = destino.cursor()

# Cria a tabela produto
cd.execute("""
CREATE TABLE produto (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    subcategoria TEXT,
    preco FLOAT,
    imagem TEXT,
    descricao TEXT,
    link TEXT,
    destaque INTEGER
)
""")

# Copia apenas os 2.000 primeiros produtos válidos
co.execute("""
SELECT *
FROM produto
WHERE
    link IS NOT NULL AND TRIM(link) <> ''
    AND imagem IS NOT NULL AND TRIM(imagem) <> ''
    AND descricao IS NOT NULL AND TRIM(descricao) <> ''
    AND preco IS NOT NULL AND preco > 0
ORDER BY destaque DESC, id DESC
LIMIT 2000
""")

produtos = co.fetchall()

cd.executemany("""
INSERT INTO produto
(id,nome,categoria,subcategoria,preco,imagem,descricao,link,destaque)
VALUES (?,?,?,?,?,?,?,?,?)
""", produtos)

# Cria a tabela de cliques
cd.execute("""
CREATE TABLE cliques (
    id INTEGER PRIMARY KEY,
    produto_id INTEGER,
    click_id VARCHAR(100),
    ip VARCHAR(50),
    user_agent TEXT,
    criado_em DATETIME
)
""")

destino.commit()

print("=" * 40)
print("Banco reduzido criado com sucesso!")
print(f"Produtos copiados: {len(produtos)}")
print("=" * 40)

origem.close()
destino.close()