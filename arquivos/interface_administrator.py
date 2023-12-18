import tkinter as tk
from administrators import Administrator
from database_administrators import DatabaseAdministrators

# Class for the interface to get administrator data
class InterfaceAdministrator:
    def __init__(self):
        self.window = tk.Tk()

    # Window to receive information
    def Window(self):
        # Function for the "Register" button click
        def button_Register():
            # Send data to the Administrator class
            name = self.entry_Name.get()
            password = self.entry_Password.get()
            email = self.entry_Email.get()
            birth_date = self.entry_BirthDate.get()
            gender = self.gender_var.get()
            phone = self.entry_Phone.get()

            # Send data to the DatabaseAdministrator class
            administrator = Administrator(name, password, email, birth_date, gender, phone)
            database_administrators = DatabaseAdministrators(administrator.get_administrator())
            database_administrators.insert_data()
            

        # Basic configurations
        self.window.title("Administrator")
        self.window.configure(background="old lace")
        self.window.geometry("280x260")

        # Get name
        self.label_Name = tk.Label(self.window, text="Nome:")
        self.label_Name.configure(background="old lace")
        self.label_Name.grid(row=0, column=0, padx=5, pady=5)

        self.entry_Name = tk.Entry(self.window)
        self.entry_Name.configure(background="antique white")
        self.entry_Name.grid(row=0, column=1, padx=5, pady=5)

        # Get password
        self.label_Password = tk.Label(self.window, text="Senha:")
        self.label_Password.configure(background="old lace")
        self.label_Password.grid(row=1, column=0, padx=5, pady=5)

        self.entry_Password = tk.Entry(self.window, show="*")
        self.entry_Password.configure(background="antique white")
        self.entry_Password.grid(row=1, column=1, padx=5, pady=5)

        # Get email
        self.label_Email = tk.Label(self.window, text="E-mail:")
        self.label_Email.configure(background="old lace")
        self.label_Email.grid(row=2, column=0, padx=5, pady=5)

        self.entry_Email = tk.Entry(self.window)
        self.entry_Email.configure(background="antique white")
        self.entry_Email.grid(row=2, column=1, padx=5, pady=5)

        # Get birth date
        self.label_BirthDate = tk.Label(self.window, text="Data de Nascimento:")
        self.label_BirthDate.configure(background="old lace")
        self.label_BirthDate.grid(row=3, column=0, padx=5, pady=5)

        self.entry_BirthDate = tk.Entry(self.window)
        self.entry_BirthDate.configure(background="antique white")
        self.entry_BirthDate.grid(row=3, column=1, padx=5, pady=5)

        # Get gender
        self.label_Gender = tk.Label(self.window, text="Gênero:")
        self.label_Gender.configure(background="old lace")
        self.label_Gender.grid(row=4, column=0, padx=5, pady=5)

        self.gender_var = tk.StringVar()

        self.radio_male = tk.Radiobutton(self.window, text="Masculino", variable=self.gender_var, value="Masculino")
        self.radio_male.configure(background="old lace")
        self.radio_male.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

        self.radio_female = tk.Radiobutton(self.window, text="Feminino", variable=self.gender_var, value="Feminino")
        self.radio_female.configure(background="old lace")
        self.radio_female.grid(row=5, column=1, padx=5, pady=5, sticky=tk.E)

        # Get phone
        self.label_Phone = tk.Label(self.window, text="Telefone:")
        self.label_Phone.configure(background="old lace")
        self.label_Phone.grid(row=6, column=0, padx=5, pady=5)

        self.entry_Phone = tk.Entry(self.window)
        self.entry_Phone.configure(background="antique white")
        self.entry_Phone.grid(row=6, column=1, padx=5, pady=5)

        # Buttons "Enter" and "Register"
        self.button_Enter = tk.Button(self.window, text="Entrar")
        self.button_Enter.configure(background="powder blue")
        self.button_Enter.grid(row=7, column=0, padx=5, pady=5)

        self.button_Register = tk.Button(self.window, text="Registrar", command=button_Register)
        self.button_Register.configure(background="powder blue")
        self.button_Register.grid(row=7, column=1, padx=5, pady=5)

        self.window.mainloop()

