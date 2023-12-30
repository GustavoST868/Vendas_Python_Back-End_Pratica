import tkinter as tk
class InteraceRegisterProduct:
    def __init__(self):
        self.window = tk.Tk()


    def Window(self):

        self.window.configure(background="#C7BEBE")

        self.label_name = tk.Label(self.window,text="Nome")
        self.label_name.configure(background="#C7BEBE")
        self.label_name.grid(row=0,column=0,padx=5,pady=5)

        self.entry_name = tk.Entry(self.window)
        self.entry_name.configure(background="#DAD6D6")
        self.entry_name.grid(row=0,column=1,padx=5,pady=5)

        self.label_price = tk.Label(self.window,text="Preço")
        self.label_price.configure(background="#C7BEBE")
        self.label_price.grid(row=1,column=0,padx=5,pady=5)

        self.entry_price = tk.Entry(self.window)
        self.entry_price.configure(background="#DAD6D6")
        self.entry_price.grid(row=1,column=1,padx=5,pady=5)

        self.label_size = tk.Label(self.window,text="Tamanho")
        self.label_size.configure(background="#C7BEBE")
        self.label_size.grid(row=2,column=0,padx=5,pady=5)

        self.entry_size = tk.Entry(self.window)
        self.entry_size.configure(background="#DAD6D6")
        self.entry_size.grid(row=2,column=1)

        self.label_description = tk.Label(self.window,text="Descrição")
        self.label_description.configure(background="#C7BEBE")
        self.label_description.grid(row=3,column=0,padx=5,pady=5)

        self.entry_description = tk.Entry(self.window)
        self.entry_description.configure(background="#DAD6D6")
        self.entry_description.grid(row=3,column=1)

        self.button_back = tk.Button(self.window,text="Voltar")
        self.button_back.configure(background="#A89E9E")
        self.button_back.grid(row=4,column=0,padx=5,pady=5)

        self.button_next = tk.Button(self.window,text="Voltar")
        self.button_next.configure(background="#A89E9E")
        self.button_next.grid(row=4,column=1,padx=5,pady=5)


        self.window.title("")
        self.window.mainloop()

i = InteraceRegisterProduct()
i.Window()