import sys
sys.path.append(".\\src")


class Pessoa:
    def __init__(self,id, nome, idade, telefone, endereco):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.endereco = endereco

class Cliente(Pessoa):
    def __init__(self,id, nome, idade, telefone, endereco, cpf):
        super().__init__(id,nome, idade, telefone, endereco)
        self.cpf = cpf

class Fornecedor(Pessoa):
    def __init__(self, id, nome, idade, telefone, endereco, marca_fornece):
        super().__init__(id, nome, idade, telefone, endereco)
        self.marca_fornece = marca_fornece

        
class Funcionario(Pessoa):
    def __init__(self, id, nome, idade, telefone, endereco, clt, funcao):
        super().__init__(id, nome, idade, telefone, endereco)
        self.clt = clt
        self.funcao = funcao
