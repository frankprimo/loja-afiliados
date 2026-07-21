import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
SELECT nome, link
FROM produto
LIMIT 10
""")

for nome, link in cursor.fetchall():
    print("=" * 80)
    print("Produto:", nome)
    print("Link:", link)

conn.close()