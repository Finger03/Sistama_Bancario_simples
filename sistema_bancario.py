menu = '''
Menu

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> Digite valor da operação que deseja executar!
'''

saldo = 0
limite = 500
extrato = ''
saques_diario = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == '1':
        valor = float(input('Valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito de: R$ {valor:.2f}\n'
            print(f'Deposito efetuado no valor de: R$ {valor:.2f}')

        else:
            print('Opração falhou. O valor informado não é válido.')

    elif opcao == '2':
        valor = float(input('Valor do saque: '))

        if valor > saldo:
            print('Operação falhou! Saldo insuficiente.')

        elif valor > limite:
            print('Operação falhou! Valor do saque maior que o seu limite.')

        elif saques_diario >= LIMITE_SAQUES:
            print('Operação falhou! Limite de saques excedido.')

        elif valor > 0:
            saldo -= valor
            saques_diario +=1
            extrato += f'Saque de: R$ {valor:.2f}\n'
            print(f'Saque efetuado no valor de: R${valor:.2f}. Você ainda pode efetuar um total de {LIMITE_SAQUES - saques_diario} saques hoje.')

        else:
            print('Operação falhou! O valor informado não é válido.')

    elif opcao == '3':
        print('========= Extrato =========\n')
        print('Nenhuma movimentação encontrada.' if not extrato else extrato)
        print(f'\nSaldo na conta: R${saldo:.2f}')
        print('===========================')

    elif opcao == '0':
        print('Obrigado por utilizar os serviços do nosso banco, tenha um bom dia!')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada')