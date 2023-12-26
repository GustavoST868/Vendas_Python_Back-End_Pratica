import tkinter as tk

class GetAddress:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):

        self.label_country = tk.Label(self.window,text="Pais")
        self.label_country.grid(row=0,column=0,padx=10,pady=10)

        self.label_state = tk.Label(self.window,text="Estado")
        self.label_state.grid(row=1,column=0,padx=10,pady=10)

        self.label_city = tk.Label(self.window,text="Cidade")
        self.label_city.grid(row=2,column=0,padx=10,pady=10)
        
        self.label_street = tk.Label(self.window,text="Rua")
        self.label_street.grid(row=3,column=0,padx=10,pady=10)

        self.label_number = tk.Label(self.window,text="Número")
        self.label_number.grid(row=4,column=0,padx=10,pady=10)

        self.label_cep = tk.Label(self.window,text="Cep")
        self.label_cep.grid(row=4,column=0,padx=10,pady=10)

        self.label_complement = tk.Label(self.window,text="Complemento")
        self.label_complement.grid(row=5,column=0,padx=10,pady=10)
        


        self.window.title("")
        self.window.mainloop()