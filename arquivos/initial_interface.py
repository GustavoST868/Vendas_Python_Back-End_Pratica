import interface_administrator_register 
import interface_user_register 
import tkinter as tk

class InitialInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.create_window()

    def create_window(self):
        def button_user():
            self.window.destroy()
            user = interface_user_register.InterfaceUser()
            user.create_window()
           
            
    
        def button_administrator():
            self.window.destroy()
            administrators = interface_administrator_register.InterfaceAdministrator()
            administrators.Window()
           
        
        self.window.title("Tipo de Usuário")
        self.window.configure(background="old lace")

        self.label = tk.Label(self.window,text="Selecione o tipo do usuário:")
        self.label.configure(background="old lace")
        self.label.grid(row=0,column=0,padx=5,pady=5)
        

        self.button_user = tk.Button(self.window, text="Usuário", command=button_user)
        self.button_user.configure(background="powder blue")
        self.button_user.grid(row=1, column=0, padx=5, pady=5)

        self.button_administrator = tk.Button(self.window, text="Administrador", command=button_administrator)
        self.button_administrator.configure(background="powder blue")
        self.button_administrator.grid(row=1, column=1, padx=5, pady=5)

        self.window.mainloop()
