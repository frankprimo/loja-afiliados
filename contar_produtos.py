import sqlite3

for banco in ["database.db", "database_reduzido.db"]:
    conn = sqlite3.connect(banco)
    cursor = conn.cursor()

    print("\nBANCO:", banco)

    cursor.execute("SELECT COUNT(*) FROM produto")
    print("Produtos:", cursor.fetchone()[0])

    conn.close()