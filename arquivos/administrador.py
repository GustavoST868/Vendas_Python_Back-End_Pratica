class Administrador:
    def __init__(self,nome,senha,email,data_nascimento,genero,telefone):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.telefone = telefone


    def Administrador(self):
        Administrador = f'''
        nome:{self.nome}
        senha:{self.senha}
        email:{self.email}
        data_nascimento:{self.data_nascimento}
        genero:{self.genero}
        telefone:{self.telefone}        
        '''
        return Administrador


