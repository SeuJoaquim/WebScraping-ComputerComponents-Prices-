import sqlite3

class Storage:     
    def __init__(self):
        self.conexao = sqlite3.connect('src/module/data/storage.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists storage (
                    id integer primary key autoincrement ,
                    name text,
                    actual_price float,
                    lower_price float,
                    ideal_price float,
                    URL text)""")
        self.conexao.commit()
        c.close()
