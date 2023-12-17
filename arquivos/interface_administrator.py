import tkinter as tk
import administrators
import database_administrators

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
                birth_data = self.entry_BirthDate.get()
                gender = self.gender_var.get()
                phone = self.entry_Phone.get()
        
                # Send data to the DatabaseAdministrator class
                administrator = administrators.Administrator(name,password,email,birth_data,gender,phone)
                Database_administrators = database_administrators.DatabaseAdministrators(administrator.get_administrator())
               
        #basic configurations
        self.window.title("Administrator")
        self.window.configure(background="gray90")
        self.window.geometry("290x260")

        # Get name
        self.label_Name = tk.Label(self.window, text="Name:")
        self.label_Name.configure(background="gray90")
        self.label_Name.grid(row=0, column=0, padx=5, pady=5)

        self.entry_Name = tk.Entry(self.window)
        self.entry_Name.grid(row=0, column=1, padx=5, pady=5)

        # Get password
        self.label_Password = tk.Label(self.window, text="Password:")
        self.label_Password.configure(background="gray90")
        self.label_Password.grid(row=1, column=0, padx=5, pady=5)

        self.entry_Password = tk.Entry(self.window, show="*")
        self.entry_Password.grid(row=1, column=1, padx=5, pady=5)

        # Get email
        self.label_Email = tk.Label(self.window, text="E-mail:")
        self.label_Email.configure(background="gray90")
        self.label_Email.grid(row=2, column=0, padx=5, pady=5)

        self.entry_Email = tk.Entry(self.window)
        self.entry_Email.grid(row=2, column=1, padx=5, pady=5)

        # Get birth date
        self.label_BirthDate = tk.Label(self.window, text="Birth Date:")
        self.label_BirthDate.configure(background="gray90")
        self.label_BirthDate.grid(row=3, column=0, padx=5, pady=5)

        self.entry_BirthDate = tk.Entry(self.window)
        self.entry_BirthDate.grid(row=3, column=1, padx=5, pady=5)

        # Get gender
        self.label_Gender = tk.Label(self.window, text="Gender:")
        self.label_Gender.configure(background="gray90")
        self.label_Gender.grid(row=4, column=0, padx=5, pady=5)

        self.gender_var = tk.StringVar()

        self.radio_male = tk.Radiobutton(self.window, text="Male", variable=self.gender_var, value="Male")
        self.radio_male.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

        self.radio_female = tk.Radiobutton(self.window, text="Female", variable=self.gender_var, value="Female")
        self.radio_female.grid(row=5, column=1, padx=5, pady=5, sticky=tk.E)

        # Get phone
        self.label_Phone = tk.Label(self.window, text="Phone:")
        self.label_Phone.configure(background="gray90")
        self.label_Phone.grid(row=6, column=0, padx=5, pady=5)

        self.entry_Phone = tk.Entry(self.window)
        self.entry_Phone.grid(row=6, column=1, padx=5, pady=5)

        # Buttons "Enter" and "Register"
        self.button_Enter = tk.Button(self.window, text="Enter")
        self.button_Enter.configure(background="lime green")
        self.button_Enter.grid(row=7, column=0, padx=5, pady=5)

        self.button_Register = tk.Button(self.window, text="Register", command=button_Register)
        self.button_Register.configure(background="lime green")
        self.button_Register.grid(row=7, column=1, padx=5, pady=5)

        self.window.mainloop()

# Example of usage:
j = InterfaceAdministrator()
j.Window()
