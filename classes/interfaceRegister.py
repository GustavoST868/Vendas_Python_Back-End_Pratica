import tkinter as tk
import interfaceIntial as interfaceIntial 
import interfaceGetAddress as interfaceGetAddress 
import user 


class RegisterInterface:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):
        def button_back():
            self.window.destroy()

            interface_initial = interfaceIntial.IntialInterface()
            interface_initial.Window()

        def button_next():
            name = self.entry_name.get()
            password = self.entry_password.get()
            email = self.entry_email.get()
            self.window.destroy()
            get_address = interfaceGetAddress.GetAddress()
            get_address.Window()

        self.window.configure(background="#C7BEBE")
        self.window.title("")

        self.label_name = tk.Label(self.window, text="Nome")
        self.label_name.configure(background="#C7BEBE")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)

        self.entry_name = tk.Entry(self.window)
        self.entry_name.configure(background="#DAD6D6")
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = tk.Label(self.window, text="Senha")
        self.label_password.configure(background="#C7BEBE")
        self.label_password.grid(row=1, column=0, padx=10, pady=10)

        self.entry_password = tk.Entry(self.window, show="*")
        self.entry_password.configure(background="#DAD6D6")
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.label_email = tk.Label(self.window, text="Email")
        self.label_email.configure(background="#C7BEBE")
        self.label_email.grid(row=2, column=0, padx=10, pady=10)

        self.entry_email = tk.Entry(self.window)
        self.entry_email.configure(background="#DAD6D6")
        self.entry_email.grid(row=2, column=1, padx=10, pady=10)

        self.button_back = tk.Button(self.window, text="Voltar", command=button_back, relief='flat')
        self.button_back.configure(background="#A89E9E")
        self.button_back.grid(row=3, column=0, padx=10, pady=10)

        self.button_next = tk.Button(self.window, text="Próximo", relief='flat', command=button_next)
        self.button_next.configure(background="#A89E9E")
        self.button_next.grid(row=3, column=1, padx=10, pady=10)

        self.window.mainloop()


