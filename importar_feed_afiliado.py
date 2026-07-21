import pandas as pd
import sqlite3
import shutil
import os


CSV = "1005_200149_Shopee Brasil - 2022_20260721T045538_1.csv"
BANCO = "database_reduzido.db"

# Backup
if os.path.exists(BANCO):
    shutil.copy(
        BANCO,
        "database_reduzido_backup.db"
    )

print("Backup criado!")


conn = sqlite3.connect(BANCO)
cursor = conn.cursor()


df = pd.read_csv(
    CSV,
    encoding="utf-8"
)


contador = 0


for _, row in df.iterrows():

    nome = str(row.get("title", ""))

    imagem = str(row.get("image_link", ""))

    descricao = str(row.get("description", ""))

    categoria = str(row.get("global_category1", "Outros"))

    subcategoria = str(row.get("global_category2", ""))

    preco = row.get("sale_price")

    link = str(row.get("product_short link", ""))


    if not nome or not link:
        continue


    cursor.execute("""
    INSERT INTO produto
    (
        nome,
        categoria,
        subcategoria,
        preco,
        imagem,
        descricao,
        link,
        destaque
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        nome,
        categoria,
        subcategoria,
        preco,
        imagem,
        descricao,
        link,
        0
    ))


    contador += 1


conn.commit()
conn.close()


print("--------------------------------")
print("Produtos importados:", contador)
print("--------------------------------")