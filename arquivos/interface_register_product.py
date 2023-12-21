import tkinter as tk
import product
import database_product

class InterfaceProduct:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):
        self.window.title("Cadastro de Produto")
        self.window.configure(background="old lace")
          # Labels
        self.label_name = tk.Label(self.window, text="Name:")
        self.label_name.configure(background="old lace")
        self.label_description = tk.Label(self.window, text="Description:")
        self.label_description.configure(background="old lace")
        self.label_price = tk.Label(self.window, text="Price:")
        self.label_price.configure(background="old lace")
        self.label_size = tk.Label(self.window, text="Size:")
        self.label_size.configure(background="old lace")

        # Entry widgets
        self.entry_name = tk.Entry(self.window)
        self.entry_description = tk.Entry(self.window)
        self.entry_price = tk.Entry(self.window)
        self.entry_size = tk.Entry(self.window)

        # Button to submit the form
        self.register_button = tk.Button(self.window, text="Registrar")

        # Grid layout
        self.label_name.grid(row=0, column=0, sticky=tk.E,padx=30,pady=5)
        self.label_description.grid(row=1, column=0, sticky=tk.E,padx=30,pady=5)
        self.label_price.grid(row=2, column=0, sticky=tk.E,padx=30,pady=5)
        self.label_size.grid(row=3, column=0, sticky=tk.E,padx=30,pady=5)

        self.entry_name.grid(row=0, column=1,padx=30,pady=5)
        self.entry_name.configure(background="antique white")
        self.entry_description.grid(row=1, column=1,padx=30,pady=5)
        self.entry_description.configure(background="antique white")
        self.entry_price.grid(row=2, column=1,padx=30,pady=5)
        self.entry_price.configure(background="antique white")
        self.entry_size.grid(row=3, column=1,padx=30,pady=5)
        self.entry_size.configure(background="antique white")

        self.register_button.grid(row=4, column=1,padx=30,pady=5)
        self.register_button.configure(background="powder blue")
        self.window.mainloop()

j = InterfaceProduct()
j.Window()