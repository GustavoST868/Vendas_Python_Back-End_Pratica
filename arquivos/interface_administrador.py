import tkinter as tk
import administrador
import database_administradores

class Interface_Administrador:
    def __init__(self):
        self.janela = tk.Tk()
        


    #janela para receber as informacoes
    def Janela(self):
        def botao_Cadastrar():
            Administrador = administrador.Administrador(self.entry_Nome.get(),self.entry_Senha.get(),self.entry_Email.get(),self.entry_DataNascimento.get(),self.genero_var,self.entry_Telefone.get())
            Database_administradores = database_administradores.Database_Administradores(Administrador.Administrador())
            

        self.janela.title("Administrador")
        self.janela.geometry("290x240")

        self.label_Nome = tk.Label(self.janela, text="Nome:")
        self.label_Nome.grid(row=0, column=0, padx=5, pady=5)

        self.entry_Nome = tk.Entry(self.janela)
        self.entry_Nome.grid(row=0, column=1, padx=5, pady=5)

        self.label_Senha = tk.Label(self.janela, text="Senha:")
        self.label_Senha.grid(row=1, column=0, padx=5, pady=5)

        self.entry_Senha = tk.Entry(self.janela, show="*")
        self.entry_Senha.grid(row=1, column=1, padx=5, pady=5)

        self.label_Email = tk.Label(self.janela, text="E-mail:")
        self.label_Email.grid(row=2, column=0, padx=5, pady=5)

        self.entry_Email = tk.Entry(self.janela)
        self.entry_Email.grid(row=2, column=1, padx=5, pady=5)

        self.label_DataNascimento = tk.Label(self.janela, text="Data de Nascimento:")
        self.label_DataNascimento.grid(row=3, column=0, padx=5, pady=5)

        self.entry_DataNascimento = tk.Entry(self.janela)
        self.entry_DataNascimento.grid(row=3, column=1, padx=5, pady=5)

        self.genero_var = tk.StringVar()
        self.radio_masculino = tk.Radiobutton(self.janela, text="Masculino", variable=self.genero_var, value="Masculino")
        self.radio_masculino.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

        self.radio_feminino = tk.Radiobutton(self.janela, text="Feminino", variable=self.genero_var, value="Feminino")
        self.radio_feminino.grid(row=4, column=1, padx=5, pady=5, sticky=tk.E)
        
        self.label_Telefone = tk.Label(self.janela, text="Telefone:")
        self.label_Telefone.grid(row=5, column=0, padx=5, pady=5)

        self.entry_Telefone = tk.Entry(self.janela)
        self.entry_Telefone.grid(row=5, column=1, padx=5, pady=5)

        self.botao_Entrar = tk.Button(self.janela,text="Entrar")
        self.botao_Entrar.grid(row=6, column=0, padx=5, pady=5)

        self.botao_Cadastrar = tk.Button(self.janela,text="Cadastrar",command=botao_Cadastrar)
        self.botao_Cadastrar.grid(row=6, column=1, padx=5, pady=5)


        self.janela.mainloop()

# Exemplo de uso:
j = Interface_Administrador()
j.Janela()
