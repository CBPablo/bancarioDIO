menu = '''
[1] Depositar 
[2] Sacar 
[3] Extrato 
[4] Sair
              =>'''

numero_de_depositos = 0
saldo = 0
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
valor = 0



while True:
    opcao = input(menu)
    if opcao == '1':
        valor = float(input('informe o valor do depósito.'))
        if valor > 0:
            saldo += valor 
            extrato += f'Deposito de R$:{valor} realizado.\n'
        else:
            print('Operação falhou valor informado inválido.\n')

    elif opcao == '2':
        if numero_saques <= LIMITE_SAQUES:
            numero_saques += 1
            valor = float(input('Informe o valor do saque .'))
            if valor <= saldo:
                saldo -= valor   
                extrato += f'Saque de R$:{valor} realizado.\n'
            else : 
                print('Operação falhou. Saldo insuficiente.')
        else:
            print('Operação falhou. Número de saques diários excedidos.')          

    elif opcao =='3':
        print('##########EXTRATO##########')
        print(f'Atividade da conta : \n')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Seusaldo é: R$: {float(saldo)}')
    
    if opcao == '4':
        print('O banco Pablo agradece sua preferência!')
        break