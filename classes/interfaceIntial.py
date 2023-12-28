import tkinter as tk
import interfaceRegister 
import interfaceEnter 

class IntialInterface:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):
        def button_register():
            self.window.destroy()
            interface_register = interfaceRegister.RegisterInterface()
            interface_register.Window()

        def button_enter():
            self.window.destroy()
            enter_interface = interfaceEnter.EnterInterface()
            enter_interface.Window()

        self.window.title("")
        self.window.configure(background="#FF9EF6")

        self.label = tk.Label(self.window, text="Bem vindo a Loja", font=20)
        self.label.configure(background="#FF9EF6")
        self.label.place(x=150, y=100)

        self.button_enter = tk.Button(self.window, text="Entrar", relief='flat',command=button_enter)
        self.button_enter.configure(background="#FA76ED", width=15, height=5)
        self.button_enter.place(x=50, y=300)

        self.button_register = tk.Button(self.window, text="Registrar", relief='flat', command=button_register)
        self.button_register.configure(background="#FA76ED", width=15, height=5)
        self.button_register.place(x=225, y=300)

        self.window.geometry("400x500")
        self.window.mainloop()

if __name__ == "__main__":
    interface_initial = IntialInterface()
    interface_initial.Window()
