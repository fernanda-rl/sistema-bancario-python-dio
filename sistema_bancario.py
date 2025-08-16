LIMITE_SAQUE = 500
saldo = 1000
saques_diarios = 1
extrato = ""
valor_saque = 0
valor_deposito = 0

def func_msg():
    print("\n")
    print("==============================\n")
    print("Deseja realizar outra operação?\n")
    print("[1] Sim\n")
    print("[2] Não\n")
    opcao = int(input("Digite aqui a opção desejada: \n"))
    if opcao != 1:
        print("Obrigada por escolher o sistema bancário DIO! Até mais!")
        exit()

def func_extrato():
    if extrato != "":
        print("\n")
        print("========== EXTRATO ==========")
        print(extrato)
        func_msg()
    else:
        print("========== EXTRATO ==========")
        print("Não houve nenhuma movimetação recente")
        func_msg()

def func_saque():
    global saldo, extrato, saques_diarios
    if saques_diarios <= 3:
        print("\n")
        print("========== SAQUE ==========")
        valor_saque = float(input("Digite aqui o valor do saque que deseja fazer: \n"))
        if valor_saque <= saldo and valor_saque <= LIMITE_SAQUE:
            saques_diarios += 1
            saldo -= valor_saque
            extrato += f"Saque de R$ {valor_saque} \n"
            print("Seu saldo agora é de: ", saldo)
            func_msg()
        else:
            print("Digite um valor que seja válido para saque! \n")
            return func_saque()
    else:
        print("Não é possível realizar mais nenhum saque, pois você atingiu o limite de saques diários.\n")
        func_msg()
        
def func_deposito():
    global saldo, extrato, valor_deposito
    print("\n")
    print("========== DEPÓSITO ==========")
    valor_deposito = float(input("Digite aqui o valor do depósito que deseja fazer: \n"))
    if valor_deposito >= 0.01:
        saldo += valor_deposito
        extrato += f"Depósito de R$ {valor_deposito} \n"
        print("Seu saldo agora é de: ", saldo)
        func_msg()
    else:
        print("Digite um valor que seja válido para depósito! \n")
        return func_deposito()

while True:
    print("\n")
    print("===== Seja bem vindo ao sistema bancário da DIO! ===== \n")
    print("[1] Saque\n")
    print("[2] Depósito\n")
    print("[3] Extrato\n")
    print("[4] Sair do sistema\n")
    opcao = int(input("Digite aqui a opção desejada: \n"))
    if opcao == 1:
        print("Seja bem vindo(a) ao sistema de saque! \n")
        func_saque()
    elif opcao == 2:
        print("Seja bem vindo(a) ao sistema de depósito! \n")
        func_deposito()
    elif opcao == 3:
        print("Seja bem vindo(a) ao sistema de extrato! \n")
        func_extrato()
    elif opcao == 4:
        print("Obrigada por escolher o sistema bancário DIO! Até mais!")
        break
    else:
        print("A opção digitada é inválida, tente novamente uma opção válida!")
