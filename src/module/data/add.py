from .sqlite import Storage
import tkinter as tk

class Bank(object):
    def __init__(self, name = "", actual_price = 0, lower_price = 0, ideal_price = 0, URL=""):
        self.id = 0
        self.name = name
        self.actual_price = actual_price
        self.lower_price = lower_price
        self.ideal_price = ideal_price
        self.URL = URL

    def insertItem(self):

        banco = Storage()
        try:

            c = banco.conexao.cursor()
            
            
            values = f'("{self.name}", {self.actual_price}, {self.lower_price}, {self.ideal_price}, "{self.URL}")'
            insertSyntax = """INSERT INTO storage (name, actual_price, lower_price, ideal_price, URL) VALUES """ + values
            print(insertSyntax)
            c.execute(insertSyntax)


            banco.conexao.commit()
            c.close()
            self.get_id()
            return "Sucess"
        except:
            return "Fail"

    def get_id(self):
        
        try:
            idd = f'name = "{self.name}"'
            idSyntax = """SELECT * FROM storage WHERE """ + idd
            
            banco = Storage()
            cur = banco.conexao.cursor()
            cur.execute(idSyntax)

            rows = cur.fetchone()
            self.id = rows[0]
            cur.close()
        except:
            print('Error')

    def updateItem(self):
        banco = Storage()
        try:

            c = banco.conexao.cursor()
            
            values = f'name = "{self.name}" ,actual_price = {self.actual_price}, lower_price =  {self.lower_price}'
            where = f' WHERE id = {self.id}'
            insertSyntax = """UPDATE storage SET """ + values + where
            
            print(insertSyntax)
            c.execute(insertSyntax)

            banco.conexao.commit()
            c.close()

            return "Sucess"
        except:
            return "Fail"

    def get_all_items(self):
        banco = Storage()
        cur = banco.conexao.cursor()
        cur.execute("SELECT * FROM storage")

        rows = cur.fetchall()

        return rows

