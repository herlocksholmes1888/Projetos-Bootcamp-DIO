menu = """
[nu] Novo usuário
[1] Depositar
[2] Sacar
[3] Visualizar extrato
[4] Sair
"""

saldo = 0
numero_saque = 0
numero_deposito = 0
extrato = ""
usuarios = []

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    else: 
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("Usuário criado com sucesso!")

def depositar(saldo, numero_deposito):
    saldo += dvalor
    numero_deposito += 1
    print("Valor depositado com sucesso!")
    return saldo, numero_deposito

def sacar(saldo, numero_saque):
    LIMITE_SAQUE = 500
    LIMITE_DIARIO = 3
    if saldo < svalor:
        print("Operação inválida. Não há dinheiro o suficiente na conta.")
    else: 
        if svalor <= LIMITE_SAQUE and numero_saque < LIMITE_DIARIO:
            saldo -= svalor 
            numero_saque += 1
            print(f"Você sacou R${svalor} com sucesso!")
        else:
            print("Operação inválida. Você atingiu algum limite do banco.")
    return saldo, numero_saque

while True:
    i = input(menu)

    if i == 'nu':
        criar_usuario(usuarios)
    elif i == "1":
        dvalor = float(input("Quanto você deseja depositar? "))
        saldo, numero_deposito = depositar(saldo, numero_deposito)
    elif i == "2":
        svalor = float(input("Quanto você deseja sacar? "))
        saldo, numero_saque = sacar(saldo, numero_saque)
    elif i == "3":
        print(f"O seu saldo atual é de R$ {saldo}. Você realizou {numero_deposito} depósitos e {numero_saque} saques.")
    elif i == "4":
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
