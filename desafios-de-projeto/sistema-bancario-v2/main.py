import func
import settings




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
    
    #sacar
    elif opcao == 2: 
        print("[2] Saque Selecionado")
        valor = int(input("Informe o valor desejado para saque: R$"))
        
        func.sacar(
            saldo=settings.saldo,
            valor=settings.valor,
            extrato=func.exibir_extrato(),
            limite=settings.limite,
            numero_saques=settings.numero_saques,
            limite_saques=settings.LIMITE_SAQUES
            )
        
    elif opcao == 3: #extrato
        print("[3] Extrato Selecionado.")
        print("==================== EXTRATO ====================")
        
        for op in extrato:
            print(op, end="")
            
        print(f"\nSaldo atual: R$ {saldo:.2f}\n")
        print("=================================================")

    else:
        print("Operação inválida! Por favor, selecione a operação desejada.")