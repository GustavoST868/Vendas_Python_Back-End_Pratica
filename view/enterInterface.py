import tkinter as tk

class EnterInterface:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):

        self.window.configure(background="#FF9EF6")

        self.label_user = tk.Label(self.window, text="Usuário")
        self.label_user.configure(background="#FF9EF6")
        self.label_user.grid(row=0, column=0, padx=10, pady=10)

        self.entry_user = tk.Entry(self.window)
        self.entry_user.configure(background="#F2B0FC")
        self.entry_user.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = tk.Label(self.window, text="Senha")
        self.label_password.configure(background="#FF9EF6")
        self.label_password.grid(row=1, column=0, padx=10, pady=10)

        self.entry_password = tk.Entry(self.window)
        self.entry_password.configure(background="#F2B0FC")
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.button_back = tk.Button(self.window, text="Volta")
        self.button_back.configure(background="#FA76ED")
        self.button_back.grid(row=2, column=0, padx=10, pady=10)

        self.button_next = tk.Button(self.window, text="Próxima")
        self.button_next.configure(background="#FA76ED")
        self.button_next.grid(row=2, column=1, padx=10, pady=10)

        self.window.title("")
        self.window.mainloop()
