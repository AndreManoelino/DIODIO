menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saque = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Deposito")
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: +{valor}\n'
        else:
            print("Valor inválido. O valor deve ser maior que zero.")

    elif opcao == "2":
        print("Saque")
        if numero_saques < limite_saque:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor > 0:
                if saldo >= valor:
                    saldo -= valor
                    extrato += f'Saque: -{valor}\n'
                    numero_saques += 1
                else:
                    print("Saldo insuficiente.")
            else:
                print("Valor inválido. O valor deve ser maior que zero.")
        else:
            print("Limite de saques diários atingido.")

    elif opcao == "3":
        print("Extrato:")
        print(extrato)
        print(f"Saldo: {saldo}")
        print(f"Limite de saque diário restante: {limite_saque - numero_saques}")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
