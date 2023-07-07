def menu():
    opcao = input(
        '''
        SELECIONE UMA OPÇÃO ABAIXO:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    '''
    )
    return opcao
    
def conta_bancaria():
    saldo_em_conta = 0
    LIMITE_SAQUES_DIARIO = 3
    limite_saldo_saque = 500
    saques_realizados = []
    movimentacaos = []
    saques_feitos = 0

    while True:
        opcao = menu()
        if opcao == 'd':
            valor = float(input("Informe o valor a ser depositado : "))
            if valor > 0:
                saldo_em_conta += valor
                movimentacaos.append(f"Depósito: R$ {valor}")
            else:
                print("Operação falhou, valor informado é inválido")
            
        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > saldo_em_conta
            excedeu_saldo_limite = valor > limite_saldo_saque
            excedeu_limite = saques_feitos >= LIMITE_SAQUES_DIARIO

            if excedeu_saldo:
                print("Operação falhou, você não tem saldo suficiente")
            elif excedeu_saldo_limite:
                print("Operação falhou, o valor excede o limite")
            elif excedeu_limite:
                print("Limite de tentativas excedida")
            else:
                saldo_em_conta -= valor
                print("Realizado o saque...")
                saques_realizados.append(valor)
                movimentacaos.append(f"Saque: R$ {valor}")
                print("Saque efetivado, retire seu dinheiro")
        elif opcao == 'e': ##usando for para percorrer uma lista
                for movimentacao in movimentacaos:
                    print(f'{movimentacao}')
        else:
            print("Agradecemos")
            quit()

conta_bancaria()