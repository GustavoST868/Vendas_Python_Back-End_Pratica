import interface_administrator,interface_user,tkinter as tk
class Initial_Interface:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):
        self.window.geometry("200x200")

        self.button_user = tk.Button(self.window,text="Usuário")
        self.button_user.grid(row=0,column=0,padx=5,pady=5)


        self.button_administrator = tk.Button(self.window,text="Administrador")
        self.button_administrator.grid(row=1,column=0,padx=5,pady=5)


        self.window.mainloop()