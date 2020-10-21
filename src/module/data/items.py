import sqlite3
from sqlite import Storage

banco = Storage()
cur = banco.conexao.cursor()
cur.execute("SELECT * FROM storage")
rows = cur.fetchall()

for item in rows:
    print('\nTitle',item[1])
    print('\nActual_Price',item[2])
    print('\nLower_Price',item[3])
    print('\nIdeal_Price',item[4])
    print('\nUrl',item[5])
    print('\n=========================')
    print('\n')
    