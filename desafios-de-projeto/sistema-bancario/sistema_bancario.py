menu = """
################### Menu Principal ###################

Bem-vindo ao PyBank. Escolha a operação desejada

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

operacao = 0

while True:
    opcao = int(input(menu))

    if opcao == 0: #sair do sistema
        print("Obrigado por utilizar nossos serviços. Volte sempre!")
        break

    elif opcao == 1: #depositar
        deposito = int(input("Quanto você gostaria de depositar? "))

        if deposito <= 0:
            print("O valor a ser depositado deve ser positivo")

        elif deposito > 0:
            saldo += deposito
            operacao += 1
            mensagem_extrato = f"\nOperação 00{operacao}:\n\t{'Tipo da Operação:':<{25}}[1] Depósito \n\t{'Valor da Operação:':<{25}}R$ +{deposito:.2f} \n\t{'Saldo Após Operação:':<{25}}R$ {saldo:.2f}\n"
            extrato += mensagem_extrato

            print(f"A quantia de R$ {deposito:.2f} foi depositada em sua conta. \nSaldo atual: R$ {saldo:.2f}")

    elif opcao == 2: #sacar
        print("[2] Saque Selecionado")
        saque = int(input("Informe o valor desejado para saque: R$"))

        if saque > limite: #se o valor para saque for maior que o limite, retorna erro e pede para corrigir o valor.
            print(f"O valor informado é acima do limite de R$ {limite:.2f} por saque.")
        
        elif saque <= 0: #se o valor informado para saque for negativo ou igual a 0, retorna erro e pede para corrigir o valor
            print("O valor a ser sacado deve ser positivo e maior que zero.")
      
        elif numero_saques >= LIMITE_SAQUES:
            print("Quantidade máxima de saques por dia atingida. Tente novamente daqui 24h.")

        elif saque > saldo: #verifica se o usuário tem saldo suficiente para o saque
            print("Operação não realizada. Saldo insuficiente.")
        
        elif saque <= saldo:
            saldo -= saque
            numero_saques += 1
            operacao += 1
            mensagem_extrato = f"\nOperação 00{operacao}:\n\t{'Tipo da Operação:':<{25}}[2] Saque \n\t{'Valor da Operação:':<{25}}R$ -{saque:.2f} \n\t{'Saldo Após Operação:':<{25}}R$ {saldo:.2f}\n"
            extrato += mensagem_extrato

            print(f"A quantia de R$ {saque} foi retirada da sua conta. \nSaldo atual: R$ {saldo:.2f}.\nQuantidade de saques restantes: {LIMITE_SAQUES - numero_saques}")
    
    elif opcao == 3: #extrato
        print("[3] Extrato Selecionado.")
        print("==================== EXTRATO ====================")
        
        for op in extrato:
            print(op, end="")
            
        print(f"\nSaldo atual: R$ {saldo:.2f}\n")
        print("=================================================")

    else:
        print("Operação inválida! Por favor, selecione a operação desejada.")