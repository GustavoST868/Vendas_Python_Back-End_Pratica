import tkinter as tk

class Interface_Address:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):
        def button_next():
            self.window.destroy()


        self.window.title("Endereço")

        self.label_city = tk.Label(self.window, text="Cidade:")
        self.label_city.grid(row=0, column=0, padx=5, pady=5)

        self.entry_city = tk.Entry(self.window)
        self.entry_city.grid(row=0, column=1, padx=5, pady=5)

        self.label_state = tk.Label(self.window, text="Estado:")
        self.label_state.grid(row=1, column=0, padx=5, pady=5)

        self.entry_state = tk.Entry(self.window)
        self.entry_state.grid(row=1, column=1, padx=5, pady=5)

        self.label_neighborhood = tk.Label(self.window, text="Bairro:")
        self.label_neighborhood.grid(row=2, column=0, padx=5, pady=5)

        self.entry_neighborhood = tk.Entry(self.window)
        self.entry_neighborhood.grid(row=2, column=1, padx=5, pady=5)

        self.label_country = tk.Label(self.window, text="Pais:")
        self.label_country.grid(row=3, column=0, padx=5, pady=5)

        self.entry_country = tk.Entry(self.window)
        self.entry_country.grid(row=3, column=1, padx=5, pady=5)

        self.label_number = tk.Label(self.window, text="Número:")
        self.label_number.grid(row=4, column=0, padx=5, pady=5)

        self.entry_number = tk.Entry(self.window)
        self.entry_number.grid(row=4, column=1, padx=5, pady=5)

        self.label_complement = tk.Label(self.window, text="Complemento:")
        self.label_complement.grid(row=5, column=0, padx=5, pady=5)

        self.entry_complement = tk.Entry(self.window)
        self.entry_complement.grid(row=5, column=1, padx=5, pady=5)

        self.button_register = tk.Button(self.window, text="Registrar")
        self.button_register.grid(row=6, column=0, padx=5, pady=5)

        self.button_next = tk.Button(self.window, text="Próximo",command=button_next)
        self.button_next.grid(row=6, column=1, padx=5, pady=5)

        self.window.mainloop()