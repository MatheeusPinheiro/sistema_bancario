import os

menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

-->
"""

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    os.system('cls')
    print(menu)
    opc = input('Informe sua opção: ')

    if opc == 'd':
        
        os.system('cls')
        valor_deposito = input('Informe o valor que deseja depositar: ')
        valor_deposito = float(valor_deposito)

        while valor_deposito <= 0:
            os.system('cls')
            print('Valor não permitido')
            valor_deposito = input('Informe o valor que deseja depositar: ')
            valor_deposito = float(valor_deposito)
            
        if valor_deposito > 0:
            saldo+=valor_deposito
            print('Valor depositado com sucesso...😀')
        
        os.system('Pause')

    elif opc == 's':

        os.system('cls')
        print(f'Valor disponível para saque: R$ {saldo:,.2f}')

        valor_saque = input('Informe o valor que deseja sacar: ')
        valor_saque = float(valor_saque)

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            os.system('cls')
            print('Operação falhou, você nao tem saldo suficiente...')
            os.system('Pause')
        elif excedeu_limite:
            os.system('cls')
            print('Operação falhou, o valor do saque excede o limite...')
            os.system('Pause')
        elif excedeu_saques:
            os.system('cls')
            print('Operação falhou, número maximo de saques excedido...')
            os.system('Pause')
        elif valor_saque > 0:
            saldo-=valor_saque
            extrato += f'Saque R$ {valor_saque:.2f}\n'
            numero_saques+=1
        else:
            os.system('cls')
            print('Operação falhou, o valor informado é invalído...')
            os.system('Pause')



    elif opc == 'e':
        os.system('cls')
        print('############-----EXTRATO------############# \n')
        print('Não foram realizadas movimentações no período.' if not extrato else extrato)
        print(f'Saldo: {saldo:.2f}')
        print('------------------------------------------')
        os.system('Pause')
    elif opc == 'q':
        break
    else:
        os.system('cls')
        print('Opção invalida')
        os.system('Pause')
