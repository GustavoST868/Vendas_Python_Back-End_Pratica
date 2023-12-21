import tkinter as tk
import product
import database_product

class InterfaceProduct:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):
        self.window.title("Janela de Cadastro de Produto")
        self.window.mainloop()
