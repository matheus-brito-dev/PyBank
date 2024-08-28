#!/usr/bin/env python
# coding: utf-8

# In[35]:


''''
Projetinho básico de um banco em python
bootcamp engenheiro de dados - DIO
author: Matheus Brito de Oliveira
27/08/2024
saque,deposito e extrato com validações propostas

'''

def menu_bank():
    decorator = '-'
    largura = 40
    titulo = "Bem vindo ao PyBank"
    return f"{titulo.center(largura,decorator)}\n\n[1] - Depositar\n[2]-Sacar\n[3]-Ver Extrato\n[4]-Sair";

print(menu_bank())
saldo = 0
extrato = ''
LIMITE = 500
qtd_saque = 0


while True:
    
    op = int(input("Informe sua opção "))
    
    if op == 1:
        valor = float(input("Informe o valor do depósito "))
        if valor < 1.0:
            print("Para depositar, precisa ter algum valor")
        else:
            saldo += valor
            saida_operacao = f"(+) R$ {valor} DEPÓSITO\n"
            extrato += saida_operacao
            print(f'Seu saldo é R$ {saldo}')
            
            
    elif op == 2:
        valor = float(input("Informe o valor do saque "))
        if valor > saldo:
            print("Saldo insuficiente, por favor faça um depósito antes de sacar")
        elif valor > LIMITE:
             print("Limite de saque ultrapassado, favor consultar o gerente")
        else:
            if qtd_saque < 3:
                
                saldo -= valor
                saida_operacao = f"(-) R$ {valor} SAQUE\n"
                extrato += saida_operacao
                qtd_saque+=1
            else:
                print("Limite diário de saque ultrapassado")
                
            print(f'Seu saldo é R$ {saldo}')
    elif op == 3:
        if extrato == "":
            print("Não foram realizadas movimentações")
        print(extrato)
        print()
        print(f'Seu saldo é R$ {saldo}')
    elif op == 4:
        print("O PyBank agradece sua visita, volte sempre!")
        break
    else:
        print("Opção inválida, por favor digite uma opção válida")





# In[ ]:





# In[ ]:




