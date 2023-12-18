import tkinter as tk

class User_Enter:
    def __init__(self):
        self.window = tk.Tk()



    def Window(self):
        self.window.title("User Login")

        self.name_label = tk.Label(self.window,text="Nome:")
        self.name_label.grid(row=0,column=0,padx=5,pady=5)

        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0,column=1,padx=5,pady=5)

        self.password_label = tk.Label(self.window,text="Senha:")
        self.password_label.grid(row=1,column=0,padx=5,pady=5)

        self.password_entry = tk.Entry(self.window)
        self.password_entry.grid(row=1,column=1,padx=5,pady=5)

        self.button_enter = tk.Button(self.window,text="Entrar")
        self.button_enter.grid(row=2,column=0,padx=5,pady=5)


        self.window.mainloop()