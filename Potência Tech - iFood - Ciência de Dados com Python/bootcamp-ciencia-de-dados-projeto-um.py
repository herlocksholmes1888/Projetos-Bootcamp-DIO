menu = """
[1] Depositar
[2] Sacar
[3] Visualizar extrato
[4] Sair
"""

saldo = 0
numero_saque = 0
numero_deposito = 0
extrato = ""
LIMITE_SAQUE = 500
LIMITE_DIARIO = 3

while True:
    i = input(menu)

    if i == "1":
        dvalor = float(input("Quanto você deseja depositar? "))
        saldo += dvalor
        numero_deposito += 1
        print("Valor depositado com sucesso!")
    elif i == "2":
        svalor = float(input("Quanto você deseja sacar? "))
        if saldo < svalor:
            print("Operação inválida. Não há dinheiro o suficiente na conta.")
        else: 
            if svalor <= LIMITE_SAQUE and numero_saque < LIMITE_DIARIO:
                saldo -= svalor 
                numero_saque += 1
                print("Valor sacado com sucesso!")
            else:
                print("Operação inválida. Você atingiu algum limite do banco.")
    elif i == "3":
        print(f"O seu saldo atual é de R$ {saldo}. Você realizou {numero_deposito} depósitos e {numero_saque} saques.")
    elif i == "4":
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
        