import json
import os
import sys
import sqlite3
import random
sys.path.append("..\\src")
from Model.model_pessoa import Cliente, Fornecedor, Funcionario

#Fornecedor
def cadastrar_fornecedor():
    while True:
        os.system('cls')
        print('==========CADASTRO DE FORNECEDOR ==========')
        fornecedor1 = Fornecedor(int(random.randint(1, 1000000)),
        str(input('Nome Fornecedor: ').capitalize()),
        int(input('Idade Fornecedor:')), 
        int(input('Telefone Fornecedor: ')), 
        str(input('Endereço Fornecedor: ').capitalize()), 
        str(input('Marca do Fornecedor: ')).capitalize())

        print('='*50)
        print(f'''DADOS INSERIDOS:
ID: {fornecedor1.id}
NOME: {fornecedor1.nome}
IDADE: {fornecedor1.idade}
TELEFONE: {fornecedor1.telefone}
ENDEREÇO: {fornecedor1.endereco}
MARCA_FORNECEDOR: {fornecedor1.marca_fornece}''')
        print('='*50)
        confirmar = str(input('''DESEJA CONFIRMAR O CADASTRO?? 
1- DIGITE S OU SIM PARA FINALIZAR O CADASTRO 
2- DIGITE QUALQUER TECLA PARA REFAZER O CADASTRO
R: ''').lower())
        id = fornecedor1.id
        nome = fornecedor1.nome
        idade = fornecedor1.idade
        telefone = fornecedor1.telefone
        endereco = fornecedor1.endereco
        marca = fornecedor1.marca_fornece
        lista = [id, nome, idade, telefone, endereco, marca]
        if confirmar == 's' or confirmar == 'sim':
            banco = sqlite3.connect('mercado.db')
            cursor = banco.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Fornecedor (Id INTEGER, Nome text, Idade INTEGER, Telefone INTEGER, Endereço text, Marca text);')
            cursor.execute("INSERT INTO fornecedor (Id, Nome, Idade, Telefone, Endereço, Marca) VALUES (?,?,?,?,?,?)", lista)
            banco.commit()
            os.system('cls')
            print('Fornecedor cadastrado com Sucesso!!')
            banco.close()
            break
        else:
            os.system('cls')
            pass

def alterar_fornecedor():
    os.system('cls')
    print('Fornecedor alterado com sucesso!')
    pass

def remover_fornecedor():
    os.system('cls')
    print('Fornecedor removido com sucesso!')

def consultar_fornecedor():
    os.system('cls')
    print('Fornecedores cadastrados:')

#menu_fornecedor
def menu_fornecedor():
    os.system('cls')
    while True:
        try:
            escolha_menu = int(input('''
===========GESTÃO DE FORNECEDORES=======
SELECIONE A OPÇÃO DESEJADA:
1️⃣  CADASTRAR FORNECEDOR
2️⃣  ALTERAR FORNECEDOR
3️⃣  DELETAR FORNECEDOR
4️⃣  CONSULTAR FORNECEDORES CADASTRADOS
0️⃣  SAIR OU VOLTAR AO MENU ANTERIOR
========================================
Resposta: '''))
            if escolha_menu == 1:
                cadastrar_fornecedor()
            elif escolha_menu == 2:
                alterar_fornecedor()
            elif escolha_menu == 3:
                remover_fornecedor()
            elif escolha_menu == 4:
                consultar_fornecedor()
            elif escolha_menu == 0:
                os.system('cls')
                break
            else:
                os.system('cls')
                print('🛑 FAVOR ENTRAR SOMENTE COM VALORES DO MENU: 0 ~ 4 🛑')

        except ValueError:
            os.system('cls')
            print('⛔ FAVOR ENTRAR SOMENTE COM VALORES DO MENU: 0 ~ 4 ⛔')

#Cliente
def cadastrar_cliente():
    os.system('cls')
    print('==========CADASTRO DE CLIENTE ==========')
    while True:
        cliente1 = Cliente(int(random.randint(1, 1000000)),
        str(input('Nome Cliente: ').capitalize()),
        str(input('Idade Cliente:')), 
        str(input('Telefone Cliente: ')), 
        str(input('Endereço Cliente: ').capitalize()), 
        str(input('Cpf do Cliente: ')))

        os.system('cls')
        print('='*50)
        print(f'''DADOS INSERIDOS:
ID: {cliente1.id}
NOME: {cliente1.nome}
IDADE: {cliente1.idade}
TELEFONE: {cliente1.telefone}
ENDEREÇO: {cliente1.endereco}
CPF: {cliente1.cpf}''')
        print('='*50)

        confirmar = str(input('''DESEJA CONFIRMAR O CADASTRO?? 
1- DIGITE S OU SIM PARA FINALIZAR O CADASTRO 
2- DIGITE QUALQUER TECLA PARA REFAZER O CADASTRO
R: ''').lower())
        id = cliente1.id
        nome = cliente1.nome
        idade = cliente1.idade
        telefone = cliente1.telefone
        endereco = cliente1.endereco
        cpf = cliente1.cpf
        lista = [id, nome, idade, telefone, endereco, cpf]

        if confirmar == 's' or confirmar == 'sim':
            banco = sqlite3.connect('mercado.db')
            cursor = banco.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Cliente (Id_Cliente integer, Nome text, Idade INTEGER, Telefone INTEGER, Endereço text, cpf INTEGER);')
            cursor.execute("INSERT INTO Cliente (Id_Cliente, Nome, Idade, Telefone, Endereço, Cpf) VALUES(?,?,?,?,?,?)", lista)
            banco.commit()
            os.system('cls')
            print('Cliente cadastrado com Sucesso!!')
            banco.close()
            break
        else:
            os.system('cls')
            pass


def alterar_cliente():
    os.system('cls')
    print('Cliente alterado com sucesso!')

def remover_cliente():
    os.system('cls')
    print('Cliente removido com sucesso!')

def consultar_cliente():
    os.system('cls')
    print('Clientes cadastrados: ')

#menu_cliente
def menu_cliente():
    os.system('cls')
    while True:
        try:
            escolha_menu = int(input('''
===========GESTÃO DE CLIENTES===========
SELECIONE A OPÇÃO DESEJADA:
1️⃣  CADASTRAR CLIENTE
2️⃣  ALTERAR CLIENTE
3️⃣  DELETAR CLIENTE
4️⃣  CONSULTAR CLIENTES CADASTRADOS
0️⃣  SAIR
========================================
Resposta: '''))
            if escolha_menu == 1:
                os.system('cls')
                cadastrar_cliente()
            elif escolha_menu == 2:
                os.system('cls')
                alterar_cliente()
            elif escolha_menu == 3:
                os.system('cls')
                remover_cliente()
            elif escolha_menu == 4:
                os.system('cls')
                consultar_cliente()
            elif escolha_menu == 0:
                os.system('cls')
                break
            else:
                os.system('cls')
                print('🛑 FAVOR ENTRAR SOMENTE COM VALORES DO MENU: 0 ~ 4 🛑')

        except ValueError:
            os.system('cls')
            print('⛔ FAVOR ENTRAR SOMENTE COM VALORES DO MENU: 0 ~ 4 ⛔')

#Funcionario
def cadastrar_funcionario():
    os.system('cls')
    print('==========CADASTRO DE FUNCIONÁRIO ==========')
    while True:
        funcionario1 = Funcionario(int(random.randint(1, 1000000)),
        str(input('Nome funcionario: ').capitalize()),
        int(input('Idade funcionario: ')), 
        int(input('Telefone funcionario: ')), 
        str(input('Endereço funcionario: ').capitalize()), 
        str(input('Cargo do funcionario: ').capitalize()),
        str(input('Função do funcionario: ').capitalize()))

        os.system('cls')
        print('='*50)
        print(f'''DADOS INSERIDOS:
ID: {funcionario1.id}
NOME: {funcionario1.nome}
IDADE: {funcionario1.idade}
TELEFONE: {funcionario1.telefone}
ENDEREÇO: {funcionario1.endereco}
CARGO: {funcionario1.clt}
FUNÇÃO: {funcionario1.funcao}''')
        print('='*50)

        confirmar = str(input('''DESEJA CONFIRMAR O CADASTRO?? 
1- DIGITE S OU SIM PARA FINALIZAR O CADASTRO 
2- DIGITE QUALQUER TECLA PARA REFAZER O CADASTRO
R: ''').lower())
        id = funcionario1.id
        nome = funcionario1.nome
        idade = funcionario1.idade
        telefone = funcionario1.telefone
        endereco = funcionario1.endereco
        cargo = funcionario1.clt
        funcao = funcionario1.funcao
        lista = [id, nome, idade, telefone, endereco, cargo, funcao]
        if confirmar == 's' or confirmar == 'sim':
            banco = sqlite3.connect('mercado.db')
            cursor = banco.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Funcionários (ID INTEGER, Nome text, Idade INTEGER, Telefone INTEGER, Endereço text, Cargo text, Função text);')
            cursor.execute("INSERT INTO Funcionários (ID, Nome, Idade, Telefone, Endereço, Cargo, Função) VALUES (?,?,?,?,?,?,?)", lista)
            banco.commit()
            os.system('cls')
            print('Funcionário cadastrado com Sucesso!!')
            banco.close()
            break

        elif confirmar == 'sair':
            pass
        else:
            os.system('cls')
            pass

def alterar_funcionario():
    os.system('cls')
    print('Funcionario alterado com sucesso!')

def remover_funcionario():
    os.system('cls')
    print('Funcionario removido com sucesso!')

def consultar_funcionario():
    os.system('cls')
    with open ('funcionario.json', 'r') as arquivo:
        dados = json.load(arquivo)
    print(dados)

#menu_funcionario
def menu_funcionario():
    os.system('cls')
    while True:
        try:
            escolha_menu = int(input('''
===========GESTÃO DE FUNCIONÁRIOS=======
SELECIONE A OPÇÃO DESEJADA:
1️⃣  CADASTRAR FUNCIONÁRIO
2️⃣  ALTERAR FUNCIONÁRIO
3️⃣  DELETAR FUNCIONÁRIO
4️⃣  CONSULTAR FUNCIONÁRIOS CADASTRADOS
0️⃣  SAIR
========================================
Resposta: '''))
            if escolha_menu == 1:
                cadastrar_funcionario()
            elif escolha_menu == 2:
                alterar_funcionario()
            elif escolha_menu == 3:
                remover_funcionario()
            elif escolha_menu == 4:
                consultar_funcionario()
            elif escolha_menu == 0:
                os.system('cls')
                break
            else:
                os.system('cls')
                print('🛑 FAVOR ENTRAR SOMENTE COM VALORES DO MENU: 0 ~ 4 🛑')

        except ValueError:
            os.system('cls')
            print('⛔ FAVOR ENTRAR SOMENTE COM VALORES DO MENU: 0 ~ 4 ⛔')
