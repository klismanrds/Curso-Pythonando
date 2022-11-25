import json
import os
import sys
import sqlite3
import random
sys.path.append("..\\src")
from Model.model_produto import Estoque, Produto
# from Controller.controller import banco_de_dados_produto

def cadastrar_produto():
    print('==========CADASTRO DE PRODUTO ==========')
    while True:
        produto1 = Estoque(int(random.randint(1, 1000000)),
        str(input('Nome produto: ')),
        float(input('Preço produto:')), 
        str(input('Categoria produto: ')),
        str(input('Quantidade: ')))

        print('='*50)
        print(f'''DADOS INSERIDOS:
NOME: {produto1.nome}
PREÇO: {produto1.preco}
CATEGORIA: {produto1.categoria}''')
        print('='*50)

        confirmar = str(input('''DESEJA CONFIRMAR O CADASTRO?? 
1- DIGITE S OU SIM PARA FINALIZAR O CADASTRO 
2- DIGITE QUALQUER TECLA PARA REFAZER O CADASTRO
R: ''').lower())
        id = produto1.id
        nome = produto1.nome
        preco = produto1.preco
        categoria = produto1.categoria
        lista = [id, nome, preco, categoria]
        if confirmar == 's' or confirmar == 'sim':
            banco = sqlite3.connect('mercado.db')
            cursor = banco.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS produto (Id_Produto text, Nome text, Preço REAL, Categoria text);')
            cursor.execute("INSERT INTO produto (Id_Produto, Nome, Preço, Categoria) VALUES (?,?,?,?)", lista)
            banco.commit()
            os.system('cls')
            print('Produto cadastrado com Sucesso!!')
            banco.close()
            break
        else:
            os.system('cls')
            pass



def alterar_produto():
    os.system('cls')
    print('Produto alterado com sucesso')
    pass

def remover_produto():
    os.system('cls')
    print('Produto removido com sucesso')
    pass

def consultar_produto():
    os.system('cls')
    print('Produtos cadastrados: ')
    pass

def menu_produto():
    while True:
        try:
            escolha_menu = int(input('''
===========GESTÃO DE PRODUTOS===========
SELECIONE A OPÇÃO DESEJADA:
1️⃣  CADASTRAR PRODUTO
2️⃣  ALTERAR PRODUTO
3️⃣  DELETAR PRODUTO
0️⃣  SAIR OU VOLTAR AO MENU ANTERIOR
========================================
Resposta: '''))
            if escolha_menu == 1:
                cadastrar_produto()
            elif escolha_menu == 2:
                alterar_produto()
            elif escolha_menu == 3:
                remover_produto()
            elif escolha_menu == 4:
                consultar_produto()
            elif escolha_menu == 0:
                os.system('cls')
                break
            else:
                os.system('cls')
                print('🛑 FAVOR ENTRAR SOMENTE COM VALORES DO MENU: 0 ~ 4 🛑')

        except ValueError:
            os.system('cls')
            print('⛔ FAVOR ENTRAR SOMENTE COM VALORES DO MENU: 0 ~ 4 ⛔')
