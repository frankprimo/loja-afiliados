import sqlite3

conn = sqlite3.connect("database_reduzido.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(produto)")

for coluna in cursor.fetchall():
    print(coluna)

conn.close()