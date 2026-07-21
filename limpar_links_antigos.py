import sqlite3

BANCO = "database_reduzido.db"

conn = sqlite3.connect(BANCO)
cursor = conn.cursor()

antes = cursor.execute(
    "SELECT COUNT(*) FROM produto"
).fetchone()[0]

print("Produtos antes:", antes)

cursor.execute("""
DELETE FROM produto
WHERE link LIKE 'https://shopee.com.br/product/%'
""")

conn.commit()

depois = cursor.execute(
    "SELECT COUNT(*) FROM produto"
).fetchone()[0]

print("Produtos depois:", depois)

conn.close()