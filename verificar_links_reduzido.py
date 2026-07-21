import sqlite3

conn = sqlite3.connect("database_reduzido.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM produto")
total = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(*)
FROM produto
WHERE link IS NOT NULL AND link <> ''
""")
com_link = cursor.fetchone()[0]

cursor.execute("""
SELECT nome, link
FROM produto
LIMIT 5
""")

exemplos = cursor.fetchall()

print("Total produtos:", total)
print("Produtos com link:", com_link)

print("\nExemplos:")
for nome, link in exemplos:
    print("----------------")
    print(nome)
    print(link)

conn.close()