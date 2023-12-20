import os
import tkinter as tk


class Intermediate_Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.img_path = "C:/Users/Gustavo/Downloads/POO_Vendas/arquivos/camisa.png"
        self.imagens = []  

    def on_image_click(self, index):
        print(f"Imagem {index + 1} clicada!")

    def Window(self):
        self.window.title("Janela de Produtos")
        self.window.geometry("500x600")

        try:
            i = 0
            x = 20
            y = 20
            while i < 4:
                imagem = tk.PhotoImage(file=self.img_path)
                self.imagens.append(imagem)  
                botao_imagem = tk.Button(self.window, image=imagem, command=lambda index=i: self.on_image_click(index))
                botao_imagem.place(x=x, y=y)
                x += 60
                i += 1
        except tk.TclError:
            print(f"Erro ao carregar a imagem: {self.img_path}")

        self.window.mainloop()


janela = Intermediate_Interface()
janela.Window()
