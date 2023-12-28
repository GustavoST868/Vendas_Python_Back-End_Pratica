import tkinter as tk
import interfaceIntial
import user

class EnterInterface:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):
        def button_back():
            self.window.destroy()
            initial_interface = interfaceIntial.IntialInterface()
            initial_interface.create_window()

        def button_next():
            username = entry_user.get()
            password = entry_password.get()
            user_instance = user.User(username, password)
            print(user_instance.user_exists(username))
            
        self.window.configure(background="#C7BEBE")

        label_user = tk.Label(self.window, text="Usuário")
        label_user.configure(background="#C7BEBE")
        label_user.grid(row=0, column=0, padx=10, pady=10)

        entry_user = tk.Entry(self.window)
        entry_user.configure(background="#DAD6D6")
        entry_user.grid(row=0, column=1, padx=10, pady=10)

        label_password = tk.Label(self.window, text="Senha")
        label_password.configure(background="#C7BEBE")
        label_password.grid(row=1, column=0, padx=10, pady=10)

        entry_password = tk.Entry(self.window)
        entry_password.configure(background="#DAD6D6")
        entry_password.grid(row=1, column=1, padx=10, pady=10)

        button_back = tk.Button(self.window, text="Volta", command=button_back)
        button_back.configure(background="#A89E9E")
        button_back.grid(row=2, column=0, padx=10, pady=10)

        button_next = tk.Button(self.window, text="Próxima", command=button_next)
        button_next.configure(background="#A89E9E")
        button_next.grid(row=2, column=1, padx=10, pady=10)

        self.window.title("")
        self.window.mainloop()


