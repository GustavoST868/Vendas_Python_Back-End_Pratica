import tkinter as tk
from tkinter import messagebox
import interfaceIntial

class InterfaceProduct:
    def __init__(self):
        self.window = tk.Tk()

    def on_image_click(self, image_number):
        message = f"Imagem {image_number} clicada"
        messagebox.showinfo("Info", message)

    def Window(self):
        def button_back():
            self.window.destroy()
            interface_initial = interfaceIntial.IntialInterface()
            interface_initial.Window()

        self.image = tk.PhotoImage(file="D:/Programação/Vendas_Python/images/tshirt.png")
        y = 20
        j = 0
        image_number = 1

        while j < 2:
            i = 0  # Reset i to 0 for each row
            x = 10

            while i < 4:
                self.label_image = tk.Label(image=self.image)
                self.label_image.place(x=x, y=y)
                self.label_image.bind("<Button-1>", lambda event, num=image_number: self.on_image_click(num))
                i += 1
                x += 260
                image_number += 1

            j += 1
            y += 270

        self.window.configure(background="#C7BEBE")
        self.label = tk.Label(self.window, text="Produtos já cadastrados:")
        self.label.configure(background="#C7BEBE")
        self.label.place(x=0, y=0)

        self.button_back = tk.Button(self.window, text="Voltar", command=button_back)
        self.button_back.configure(background="#A89E9E")
        self.button_back.place(x=10, y=570)

        self.window.title("")
        self.window.geometry("1000x600")
        self.window.mainloop()


