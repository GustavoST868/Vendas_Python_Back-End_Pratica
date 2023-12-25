import tkinter as tk

class IntialInterface:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):
        self.window.title("")
        self.window.configure(background="bisque")


        self.label = tk.Label(self.window,text="Bem vindo a Loja",font=20)
        self.label.configure(background="bisque")
        self.label.place(x=150,y=100)


        self.button_enter = tk.Button(self.window,text="Entrar",relief='flat')
        self.button_enter.configure(background="navajo white",width=15,height=5)
        self.button_enter.place(x=50,y=300)

        self.button_register = tk.Button(self.window,text="Registrar",relief='flat')
        self.button_register.configure(background="navajo white",width=15,height=5)
        self.button_register.place(x=225,y=300)



        self.window.geometry("400x500")

        self.window.mainloop()

i = IntialInterface()
i.Window()