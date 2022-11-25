import sys
import os
sys.path.append(".\\src")

from Controller.controller import sair
from Controller.controller_produto import menu_produto
from Controller.controller_pessoa import menu_cliente, menu_fornecedor, menu_funcionario
while True:
    try:
        escolha_menu = int(input('''
                 MERCEARIA
➖➖➖➖SELECIONE A OPÇÃO DESEJADA:➖➖➖➖➖

1️⃣  PRODUTO                                
2️⃣  CLIENTE                                
3️⃣  FORNECEDOR                             
4️⃣  FUNCIONÁRIO                     
5️⃣  CONSULTAR PRODUTOS CADASTRADOS  
6️⃣  CAIXA 🔸
7️⃣  RELATÓRIO DE VENDAS 🔸
8️⃣  RELATÓRIO DE CLIENTES QUE MAIS COMPRARAM 🔸

0️⃣  SAIR
=================================================
Resposta: '''))

        if escolha_menu == 1:
            os.system('cls')
            menu_produto()
            continuar = input('''PARA VOLTAR AO MENU ANTERIOR ↩ : DIGITE: S ou SIM ou VOLTAR !
❌ PARA SAIR DO PROGRAMA: DIGITE QUALQUER TECLA!!
    Resposta: ''').lower()
            if continuar == "s" or continuar == "sim" or continuar == "voltar":
                os.system('cls')
                pass
            else: 
                sair()
                break

        elif escolha_menu == 2:
            os.system('cls')
            menu_cliente()
            continuar = input('''PARA VOLTAR AO MENU ANTERIOR ↩ : DIGITE: S ou SIM ou VOLTAR !
❌ PARA SAIR DO PROGRAMA: DIGITE QUALQUER TECLA!!
    Resposta: ''').lower()
            if continuar == "s" or continuar == "sim" or continuar == "voltar":
                os.system('cls')
                pass
            else: 
                sair()
                break

        elif escolha_menu == 3:
            os.system('cls')
            menu_fornecedor()
            continuar = input('''PARA VOLTAR AO MENU ANTERIOR ↩ : DIGITE: S ou SIM ou VOLTAR !
❌ PARA SAIR DO PROGRAMA: DIGITE QUALQUER TECLA!!
    Resposta: ''').lower()
            if continuar == "s" or continuar == "sim" or continuar == "voltar":
                os.system('cls')
                pass
            else: 
                sair()
                break

        elif escolha_menu == 4:
            os.system('cls')
            menu_funcionario()
            continuar = input('''PARA VOLTAR AO MENU ANTERIOR ↩ : DIGITE: S ou SIM ou VOLTAR !
❌ PARA SAIR DO PROGRAMA: DIGITE QUALQUER TECLA!!
    Resposta: ''').lower()
            if continuar == "s" or continuar == "sim" or continuar == "voltar":
                os.system('cls')
                pass
            else: 
                sair()
                break

        elif escolha_menu >4:
            os.system('cls')
            print('⛔ FAVOR ENTRAR SOMENTE COM VALORES DO MENU: 0 ~ 8 ⛔')
            pass
        else:
            sair()
            break
    except ValueError:
        os.system('cls')
        print('⛔ FAVOR ENTRAR SOMENTE COM VALORES DO MENU: 0 ~ 8 ⛔')

#Comentando o meu código
