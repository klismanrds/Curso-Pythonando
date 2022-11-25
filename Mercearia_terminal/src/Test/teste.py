import sqlite3
import os
import sys
import random
sys.path.append(".\\src")
from Controller.controller_produto import cadastrar_produto

# from Model.model_pessoa import Cliente, Fornecedor, Funcionario
# from Model.model_produto import Estoque, Produto

# from datetime import datetime

numero = random.randint(1, 10000)
pessoa = 'Klisman'
lista = [numero, pessoa]
banco = sqlite3.connect('teste.db')
cursor = banco.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Teste_random (numero text, pessoa text NOT NULL);')
cursor.execute("INSERT INTO Teste_random (numero, pessoa) VALUES (?, ?)", lista)
banco.commit()
os.system('cls')
print('Teste funcionou com Sucesso!!')
banco.close()
