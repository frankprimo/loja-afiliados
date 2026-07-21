import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

for tabela in tabelas:
    nome = tabela[0]
    print(f"\n=== {nome} ===")

    cursor.execute(f"PRAGMA table_info({nome})")
    for coluna in cursor.fetchall():
        print(coluna)

conn.close()