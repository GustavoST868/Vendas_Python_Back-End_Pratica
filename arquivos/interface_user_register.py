import tkinter as tk
import user
import database_user
import user_enter

class InterfaceUser:
    def __init__(self):
        self.window = tk.Tk()
        self.create_window()

    def create_window(self):
        def button_register():
            self.window.destroy()
            name = self.entry_name.get()
            password = self.entry_password.get()
            email = self.entry_email.get()
            birth_date = self.entry_birth_date.get()
            gender = self.gender_var.get()
            phone = self.entry_phone.get()

            user_ = user.User(name, password, email, birth_date, gender, phone)
            db_user = database_user.DatabaseUser(user_.get_user())
            db_user.insert_data()
            


        def button_enter():
            self.window.destroy()
            enter = user_enter.User_Enter()
            enter.Window()
            

        self.window.title("Usuário")
        self.window.configure(background="old lace")
        

        self.label_name = tk.Label(self.window, text="Nome:")
        self.label_name.configure(background="old lace")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)

        self.entry_name = tk.Entry(self.window)
        self.entry_name.configure(background="antique white")
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_password = tk.Label(self.window, text="Senha:")
        self.label_password.configure(background="old lace")
        self.label_password.grid(row=1, column=0, padx=5, pady=5)

        self.entry_password = tk.Entry(self.window, show="*")
        self.entry_password.configure(background="antique white")
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        self.label_email = tk.Label(self.window, text="E-mail:")
        self.label_email.configure(background="old lace")
        self.label_email.grid(row=2, column=0, padx=5, pady=5)

        self.entry_email = tk.Entry(self.window)
        self.entry_email.configure(background="antique white")
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        self.label_birth_date = tk.Label(self.window, text="Data de Nascimento:")
        self.label_birth_date.configure(background="old lace")
        self.label_birth_date.grid(row=3, column=0, padx=5, pady=5)

        self.entry_birth_date = tk.Entry(self.window)
        self.entry_birth_date.configure(background="antique white")
        self.entry_birth_date.grid(row=3, column=1, padx=5, pady=5)

        self.label_gender = tk.Label(self.window, text="Gênero:")
        self.label_gender.configure(background="old lace")
        self.label_gender.grid(row=4, column=0, padx=5, pady=5)

        self.gender_var = tk.StringVar()

        self.radio_male = tk.Radiobutton(self.window, text="Masculino", variable=self.gender_var, value="Masculino")
        self.radio_male.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

        self.radio_female = tk.Radiobutton(self.window, text="Feminino", variable=self.gender_var, value="Feminino")
        self.radio_female.grid(row=5, column=1, padx=5, pady=5, sticky=tk.E)

        self.label_phone = tk.Label(self.window, text="Telefone:")
        self.label_phone.configure(background="old lace")
        self.label_phone.grid(row=6, column=0, padx=5, pady=5)

        self.entry_phone = tk.Entry(self.window)
        self.entry_phone.configure(background="antique white")
        self.entry_phone.grid(row=6, column=1, padx=5, pady=5)

        self.button_register = tk.Button(self.window, text="Registrar", command=button_register)
        self.button_register.configure(background="powder blue")
        self.button_register.grid(row=7, column=0, padx=5, pady=5)

        self.button_enter = tk.Button(self.window, text="Entrar",command=button_enter)
        self.button_enter.configure(background="powder blue")
        self.button_enter.grid(row=7, column=1, padx=5, pady=5)

        self.window.mainloop()