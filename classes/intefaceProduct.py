import tkinter as tk
import interfaceIntial
class InterfaceProduct:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):
        def button_back():
            self.window.destroy()
            interface_initial = interfaceIntial.IntialInterface()
            interface_initial.Window()


        self.label = tk.Label(self.window,text="Produtos disponíveis:")
        self.label.place(x=0,y=0)

        self.button_back = tk.Button(self.window,text="Voltar",command=button_back)
        self.button_back.place(x=10,y=570)

        self.window.title("")
        self.window.geometry("1000x600")
        self.window.mainloop()

i = InterfaceProduct()
i.Window()
