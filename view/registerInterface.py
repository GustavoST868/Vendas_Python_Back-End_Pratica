import tkinter as tk
import interfaceIntial

class RegisterInterface:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):
        def button_back():
            self.window.destroy()
            interface_initial = interfaceIntial.IntialInterface()
            interface_initial.Window()

        self.window.configure(background="#E676F7")
        self.window.title("")

        self.label_name = tk.Label(self.window, text="Nome")
        self.label_name.configure(background="#E676F7")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)

        self.entry_name = tk.Entry(self.window)
        self.entry_name.configure(background="#F2B0FC")
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = tk.Label(self.window, text="Senha")
        self.label_password.configure(background="#E676F7")
        self.label_password.grid(row=1, column=0, padx=10, pady=10)

        self.entry_password = tk.Entry(self.window)
        self.entry_password.configure(background="#F2B0FC")
        self.entry_password.grid(row=2, column=1, padx=10, pady=10)

        self.label_email = tk.Label(self.window, text="Email")
        self.label_email.configure(background="#E676F7")
        self.label_email.grid(row=2, column=0, padx=10, pady=10)

        self.entry_email = tk.Entry(self.window)
        self.entry_email.configure(background="#F2B0FC")
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)

        self.button_back = tk.Button(self.window, text="Voltar", command=button_back, relief='flat')
        self.button_back.configure(background="#DA30F5")
        self.button_back.grid(row=3, column=0, padx=10, pady=10)

        self.button_next = tk.Button(self.window, text="Próximo", relief='flat')
        self.button_next.configure(background="#DA30F5")
        self.button_next.grid(row=3, column=1, padx=10, pady=10)

        self.window.mainloop()


