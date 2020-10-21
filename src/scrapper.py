# External Librarys
from time import sleep 
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import asyncio



# Local files/Data files
from module.data.sqlite import Storage
from module.data.add import Bank

class Scrap(object):
    def __init__(self,time=0):
        self.time = time

    def initialize(self):
        banco = Storage()
        cur = banco.conexao.cursor()
        cur.execute("SELECT * FROM storage")
        rows = cur.fetchall()
        cur.close()

        for item in rows:
            t              = Bank()
            t.id           = item[0]
            t.name         = item[1]
            t.actual_price = item[2] 
            t.lower_price  = item[3]
            t.ideal_price  = item[4] 
            t.URL          = item[5]
            print(f"\nConectando com {item[0]}\nURL : {item[5]}")
            sleep(5)
            self.check_price_Amazon(t)


    def check_price_Amazon(self,item):
        # setting selenium to not open a Browser window
        option = Options()
        option.headless = True
        driver = webdriver.Chrome(options=option)
        driver.get(item.URL)
        print("\nCarregando página...")

        sleep(6)
        #getting the html content
        try:
            element_title = driver.find_element_by_id('productTitle')
        except:
            element_title = driver.find_element_by_id('title')

        title = element_title.get_attribute('innerHTML').strip().replace('"','').replace("'",'')

        element_price = driver.find_element_by_id("priceblock_ourprice")
        price = element_price.get_attribute('innerHTML')
        converted_price = float(price[2:10].replace('.','').replace(',','.'))

        print("Conferindo os preços...")
        
        if (item.actual_price == 0):
            # (28, '123', 100.0, 100.0, 0.0, 'tetee')
            item.name = title 
            item.actual_price = converted_price
            item.lower_price = converted_price
            item.updateItem()

        if (item.name == ''):
            item.name = title.strip().replace('"','')
            item.updateItem()

        if (item.actual_price < item.lower_price):
            item.lower_price = item.actual
            item.updateItem()

        n = False
        if (converted_price < item.ideal_price):
            n = True
            self.send_mail(item)

        if (item.actual_price != converted_price):
            item.actual_price = converted_price
            item.updateItem()

        driver.quit()
        if not n:
            print("\nPrice bigger than ideal_price ")
        print("fechando conexão...\n")


    def send_mail(self,item):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        remetente = 'igor.precos@gmail.com'
        server.login(remetente, 'kftxdrjkpcgwauva')
        subject = 'Price fell down!'
        body = f'\nProduct: {item.name}\nActual price: {item.actual_price}\nIdeal price: {item.ideal_price}\nCheck the amazon link: \n{item.URL}'

        msg = f"Subject: {subject}\n\n{body}"
        print(f"Sending email to {item.name}")
        server.sendmail(
            remetente,
            'igor.joaquim.sc@gmail.com',
            msg
        )

        print("\nEmail has been send")
        server.quit()



if __name__ == "__main__":
    t = Scrap()
    t.initialize()