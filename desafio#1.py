menu = """
    ==== MENU DE OPÇÕES ====
    (1) - Depositar
    (2) - Sacar
    (3) - Extrato
    (4) - Sair
    ========================
    Digite uma opção: 
    """
saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor a depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}"
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}")
            continue
        else:
            print("Erro! Valor inválido.")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))

        sobre_saldo = valor > saldo

        sobre_limite = valor > limite

        sobre_saques = num_saques >= LIMITE_SAQUES

        if sobre_saldo:
            print("Erro! Saldo insuficiente.")

        elif sobre_limite:
            print("Erro! Saque excede o limite.")

        elif sobre_saques:
            print("Erro! Número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"\n1Saque: R$ {valor:.2f}"
            num_saques += 1
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}")
        else:
            print("Erro! Valor inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Erro! Digite uma opção válida.")