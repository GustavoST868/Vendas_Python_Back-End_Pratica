# interface_user.py
import tkinter as tk
import user
import database_user

#Class for the interface to get user data
class InterfaceUser:
    def __init__(self):
        self.window = tk.Tk()
        self.create_window()

     # Window to receive information
    def create_window(self):
        # Function for the "Register" button click
        def button_register():
            name = self.entry_name.get()
            password = self.entry_password.get()
            email = self.entry_email.get()
            birth_date = self.entry_birth_date.get()
            gender = self.gender_var.get()
            phone = self.entry_phone.get()

            # Send data to the user class
            user_ = user.User(name, password, email, birth_date, gender, phone)
            db_user = database_user.DatabaseUser(user_.get_user())
            db_user.insert_data()
            
         # Basic configurations
        self.window.title("Usuário")
        self.window.configure(background="old lace")
        self.window.geometry("230x260")

        # Get name
        self.label_name = tk.Label(self.window, text="Name:")
        self.label_name.configure(background="old lace")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)

        self.entry_name = tk.Entry(self.window)
        self.entry_name.configure(background="antique white")
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        # Get password
        self.label_password = tk.Label(self.window, text="Password:")
        self.label_password.configure(background="old lace")
        self.label_password.grid(row=1, column=0, padx=5, pady=5)

        self.entry_password = tk.Entry(self.window, show="*")
        self.entry_password.configure(background="antique white")
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        # Get email
        self.label_email = tk.Label(self.window, text="E-mail:")
        self.label_email.configure(background="old lace")
        self.label_email.grid(row=2, column=0, padx=5, pady=5)

        self.entry_email = tk.Entry(self.window)
        self.entry_email.configure(background="antique white")
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        # Get birth date
        self.label_birth_date = tk.Label(self.window, text="Birth Date:")
        self.label_birth_date.configure(background="old lace")
        self.label_birth_date.grid(row=3, column=0, padx=5, pady=5)

        self.entry_birth_date = tk.Entry(self.window)
        self.entry_birth_date.configure(background="antique white")
        self.entry_birth_date.grid(row=3, column=1, padx=5, pady=5)

        # Get gender
        self.label_gender = tk.Label(self.window, text="Gender:")
        self.label_gender.configure(background="old lace")
        self.label_gender.grid(row=4, column=0, padx=5, pady=5)

        self.gender_var = tk.StringVar()
        
        self.radio_male = tk.Radiobutton(self.window, text="Male", variable=self.gender_var, value="Male")
        self.radio_male.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

        self.radio_female = tk.Radiobutton(self.window, text="Female", variable=self.gender_var, value="Female")
        self.radio_female.grid(row=5, column=1, padx=5, pady=5, sticky=tk.E)

         # Get phone
        self.label_phone = tk.Label(self.window, text="Phone:")
        self.label_phone.configure(background="old lace")
        self.label_phone.grid(row=6, column=0, padx=5, pady=5)

        self.entry_phone = tk.Entry(self.window)
        self.entry_Phone.configure(background="antique white")
        self.entry_phone.grid(row=6, column=1, padx=5, pady=5)

        # Buttons "Enter" and "Register"
        self.button_register = tk.Button(self.window, text="Register", command=button_register)
        self.button_register.configure(background="powder blue")
        self.button_register.grid(row=7, column=1, padx=5, pady=5)

        self.window.mainloop()


