from tkinter import *
from module.data.add import Bank

class View(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.configure(background='white')

        
        self.firstContainer = Frame(master)
        self.firstContainer['bg'] = 'white'
        self.firstContainer['pady'] = 20
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer['bg'] = 'white'
        self.secondContainer['pady'] = 0
        self.secondContainer.pack()

        self.thirdContainer = Frame(master)
        self.thirdContainer['bg'] = 'white'
        self.thirdContainer['pady'] = 40
        self.thirdContainer.pack()

        self.Url = Label(self.firstContainer, text="URL: ", bg= 'white',fg='black', width='16', borderwidth = '2')
        self.UrlInput= Entry(self.firstContainer)
        self.Url.pack(side=LEFT)
        self.UrlInput.pack(side=RIGHT)

        self.Price = Label(self.secondContainer, text="Minimum Price: ", bg= 'white',fg='black', width='16',borderwidth = '1')
        self.PriceInput= Entry(self.secondContainer)
        self.Price.pack(side=LEFT)
        self.PriceInput.pack(side=RIGHT)

        self.submit = Button(self.thirdContainer, text="Submit", bg= 'white',fg='black', width='16', borderwidth = '1')
        self.submit['command'] = self.Submit
        self.submit.pack()
    
    def Submit(self):
        Item = Bank()
        Item.URL = self.UrlInput.get()
        Item.ideal_price = self.PriceInput.get()
        print(Item.insertItem())    
        print(Item.get_all_items())
        self.UrlInput.delete(0,END)
        self.PriceInput.delete(0,END)

myapp = View()
myapp.master.title("Url and Minimum Price")

myapp.master.minsize(330,110)
myapp.mainloop()
