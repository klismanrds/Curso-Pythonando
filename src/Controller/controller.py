import json
import os
import sys
sys.path.append("..\\src")
import sqlite3
from Model.model_pessoa import Cliente, Fornecedor, Funcionario
from Model.model_produto import Estoque, Produto
from datetime import datetime

def data_e_hora():
    meses = ['','Janeiro','Fevereiro','Março','Abril','Mail','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    dia = datetime.now().day
    mes = meses[datetime.now().month]
    ano = datetime.now().year
    horas = datetime.now().hour
    minuto = datetime.now().minute
    print(f'HORA: {horas}:{minuto} | DATA: {dia} de {mes} de {ano}')
    
def alterar_produto():
    conn = sqlite3.connect('mercado.db')
    cursor = conn.cursor
    

#Sair
def sair():
    os.system('cls')
    print('SAINDO DO PROGRAMA, OBRIGADO!! ')
