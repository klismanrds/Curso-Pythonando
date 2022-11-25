#Coração da aplicação:
#Regras de Negócio, Entidades, Camada de Acesso á dados
#Classes
import sys
sys.path.append(".\\src")

class Produto:
    def __init__(self,id, nome , preco, categoria):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque(Produto):
    def __init__(self, id, nome, preco, categoria, quantidade):
        super().__init__(id, nome, preco, categoria)
        self.quantidade = quantidade
