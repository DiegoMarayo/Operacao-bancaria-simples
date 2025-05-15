'''VAMOS CRIAR UMA OPERAÇÃO BANCÁRIA SIMPLES'''

menu = """Selecione a opção:

[ D ]  Depositar
[ S ]  Sacar
[ E ]  Extrato
[ Q ]  Sair
==> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().upper()

    if opcao == "D":
            valor = float(input('Qual valor deseja depositar: '))
            if valor > 0:
                saldo += valor
                extrato += f'Depósito: R$ {valor:.2f}\n'
                print(f'\nDepósito de R$ {valor:.2f} realizado com sucesso!\n')
            else:
                print('A operação falhou! O valor informado é inválido.')

    elif opcao == 'S':
       valor = float(input('Qaual valor deseja sacar: '))
       excedeu_saldo = valor > saldo
       excedeu_limite = valor > limite
       excedeu_saques = numeros_saques >= LIMITE_SAQUES
       if excedeu_saldo:
           print('\nOperação falhou! Saldo insuficiente.\n')
       elif excedeu_limite:
           print('\nOperação falhou! O valor do saque excede o limite.\n')
       elif excedeu_saques:
           print('\nOperação falhou! Números máximo de saques excedido.\n')
       elif valor > 0:
           saldo -= valor
           extrato += f'Saque: R$ {valor:.2f}\n'
           numeros_saques += 1
           print(f'\nSaque no valor de R$ {valor:.2f} realizado com sucesso!\n')
       else:
           print('Operação falhou! O valor informado é inválido')

    elif opcao == 'E':
        print('\n========== EXTRATO ==========\n')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}\n')
        print('================================')

    elif opcao == 'Q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.\n')