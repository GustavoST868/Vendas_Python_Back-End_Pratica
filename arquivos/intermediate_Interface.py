import tkinter as tk



class Intermediate_Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.img_path = r"C:/Users/Gustavo/Downloads/POO_Vendas/arquivos/shirt.png"
        self.imagens = []  

    def on_image_click(self, index):
        print(f"Imagem {index + 1} clicada!")

    def Window(self):
        self.window.title("Janela de Produtos")
        self.window.configure(background="old lace")
        self.window.geometry("500x600")

        try:
            i1 = 0
            x1 = 20
            y1 = 20
            x2 = 20
            y2 = 150
            x3 = 20
            y3 = 280
            x4 = 20
            y4 = 410

            while i1 < 4:
                imagem = tk.PhotoImage(file=self.img_path)
                self.imagens.append(imagem)  
                botao_imagem = tk.Button(self.window, image=imagem, command=lambda index=i1: self.on_image_click(index),relief='flat')
                botao_imagem.place(x=x1, y=y1)
                x1 += 120
                i1 += 1
            
            while i1 < 8:
                imagem = tk.PhotoImage(file=self.img_path)
                self.imagens.append(imagem)  
                botao_imagem = tk.Button(self.window, image=imagem, command=lambda index=i1: self.on_image_click(index),relief='flat')
                botao_imagem.place(x=x2, y=y2)
                x2 += 120
                i1 += 1

            while i1 < 12:
                imagem = tk.PhotoImage(file=self.img_path)
                self.imagens.append(imagem)  
                botao_imagem = tk.Button(self.window, image=imagem, command=lambda index=i1: self.on_image_click(index),relief='flat')
                botao_imagem.place(x=x3, y=y3)
                x3 += 120
                i1 += 1  

            while i1 < 16:
                imagem = tk.PhotoImage(file=self.img_path)
                self.imagens.append(imagem)  
                botao_imagem = tk.Button(self.window, image=imagem, command=lambda index=i1: self.on_image_click(index),relief='flat')
                botao_imagem.place(x=x4, y=y4)
                x4 += 120
                i1 += 1  
                
        except tk.TclError:
            print(f"Erro ao carregar a imagem: {self.img_path}")


        self.button_place_order = tk.Button(self.window,text="Fazer Pedido",relief='flat')
        self.button_place_order.configure(background="powder blue")
        self.button_place_order.place(x=200,y=530,height=50,width=100)
        self.window.mainloop()



