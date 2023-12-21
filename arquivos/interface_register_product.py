import tkinter as tk
import product
import database_product

class InterfaceProduct:
    def __init__(self):
        self.window = tk.Tk()

    def run_interface(self):
        def register_button():
            product_obj = product.Product(
                self.entry_name.get(),
                self.entry_description.get(),
                self.entry_price.get(),
                self.entry_size.get()
            )
            db = database_product.DatabaseProduct(product_obj.get_product())
            db.insert_data()  # Added this line to insert data into the database

            # Modify the line below to pass the string value, not the Entry widget
            print(db.get_data(self.entry_name.get()))

        self.window.title("Cadastro de Produto")
        self.window.configure(background="old lace")

        # Labels
        labels = ["Name:", "Description:", "Price:", "Size:"]
        for i, label_text in enumerate(labels):
            label = tk.Label(self.window, text=label_text)
            label.configure(background="old lace")
            label.grid(row=i, column=0, sticky=tk.E, padx=30, pady=5)

        # Entry widgets
        self.entry_name = tk.Entry(self.window)
        self.entry_description = tk.Entry(self.window)
        self.entry_price = tk.Entry(self.window)
        self.entry_size = tk.Entry(self.window)

        entries = [self.entry_name, self.entry_description, self.entry_price, self.entry_size]
        for i, entry in enumerate(entries):
            entry.grid(row=i, column=1, padx=30, pady=5)
            entry.configure(background="antique white")

        # Button to submit the form
        self.register_button = tk.Button(self.window, text="Registrar", command=register_button)
        self.register_button.grid(row=4, column=1, padx=30, pady=5)
        self.register_button.configure(background="powder blue")

        self.window.mainloop()

# Create an instance of the InterfaceProduct class
j = InterfaceProduct()
# Call the run_interface method to start the Tkinter main loop
j.run_interface()
