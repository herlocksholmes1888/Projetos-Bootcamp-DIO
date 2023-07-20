"""
    IMPLEMENTAÇÕES FUTURAS:

    1. Associar uma quantidade de dinheiro a uma conta específica, ao invés de agir como se todos os depósitos e saques fossem feitos pelo coletivo
    2. Forçar o usuário a escrever exclusivamente números ou símbolos alfanuméricos em determinados campos
    3. Proporcionar um padrão de escrita para cada um dos campos
"""

import random

menu = """
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[ec] Entrar na conta
[1] Depositar
[2] Sacar
[3] Visualizar extrato
[4] Sair
"""

saldo = 0
numero_saque = 0
numero_deposito = 0
usuarios = []
contas = []
conta_logada = False

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

def criar_conta(usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado!")
        return
    
    senha = input("Informe sua senha: ")

    numero_conta = random.randint(1000, 9999)
    numero_conta = str(numero_conta)
    contas.append({"cpf": cpf, "numero_conta": numero_conta, "senha_conta": senha})
    print(f"Conta criada com sucesso! Seu número de conta é: {numero_conta}")

def entrar_conta(contas):
    global conta_logada
    numero_conta = input("Informe o número da conta: ")
    senha = input("Informe a senha da conta: ")

    for conta in contas:
        if conta["numero_conta"] == numero_conta and conta["senha_conta"] == senha:
            conta_logada = True
            print("Login bem-sucedido!")
            return conta

    print("Número da conta ou senha incorretos.")
    return None

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta encontrada.")
        return

    print("Contas bancárias: ")
    for conta in contas:
        print(f"CPF: {conta['cpf']}, Número da Conta: {conta['numero_conta']}")

def depositar(saldo, numero_deposito, conta_logada):
    if conta_logada is False:
        print("Faça login em uma conta antes de fazer um depósito.")
        return saldo, numero_deposito

    saldo += dvalor
    numero_deposito += 1
    print("Valor depositado com sucesso!")
    return saldo, numero_deposito

def sacar(saldo, numero_saque, conta_logada):
    LIMITE_SAQUE = 500
    LIMITE_DIARIO = 3
    if conta_logada is False:
        print("Faça login em uma conta antes de fazer um saque.")
        return saldo, numero_saque
    
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
    elif i == 'nc':
        criar_conta(usuarios, contas)
    elif i == 'lc':
        listar_contas(contas)
    elif i == 'ec':
        entrar_conta(contas)
    elif i == "1":
        if conta_logada:
            dvalor = float(input("Quanto você deseja depositar? "))
            saldo, numero_deposito = depositar(saldo, numero_deposito, conta_logada)
        else:
            print("Faça login antes de fazer um depósito.")
    elif i == "2":
        if conta_logada: 
            svalor = float(input("Quanto você deseja sacar? "))
            saldo, numero_saque = sacar(saldo, numero_saque, conta_logada)
        else: 
            print("Faça login antes de fazer um saque.")
    elif i == "3":
        if conta_logada:
            print(f"O seu saldo atual é de R$ {saldo}. Você realizou {numero_deposito} depósitos e {numero_saque} saques.")
        else:
            print("Faça login antes de ver seu extrato.")
    elif i == "4":
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
