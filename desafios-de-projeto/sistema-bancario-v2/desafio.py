def menu():
    menu = """
    ==================================== MENU PRINCIPAL ====================================

    Bem-vindo ao PyBank. Escolha a operação desejada

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo Usuário
    [7] Listar Usuários
    [0] Sair

    => """

    return int(input(menu))


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, operacao):
    # se o valor para saque for maior que o limite, retorna erro e pede para corrigir o valor.
    if valor > limite:
        print(f"O valor informado é acima do limite de R$ {limite:.2f} por saque.")

    # se o valor informado para saque for negativo ou igual a 0, retorna erro e pede para corrigir o valor
    elif valor <= 0:
        print("O valor a ser sacado deve ser positivo e maior que zero.")

    elif numero_saques >= limite_saques:
        print(
            "Quantidade máxima de saques por dia atingida. Tente novamente daqui 24h."
        )

    # verifica se o usuário tem saldo suficiente para o saque
    elif valor > saldo:
        print("Operação não realizada. Saldo insuficiente.")

    elif valor <= saldo:
        saldo -= valor
        numero_saques += 1
        operacao += 1
        mensagem_extrato = f"\nOperação 00{operacao}:\n\t{'Tipo da Operação:':<{25}}[2] Saque \n\t{'Valor da Operação:':<{25}}R$ -{valor:.2f} \n\t{'Saldo Após Operação:':<{25}}R$ {saldo:.2f}\n"
        extrato += mensagem_extrato

        print(
            f"A quantia de R$ {valor} foi retirada da sua conta. \nSaldo atual: \tR$ {saldo:.2f}.\nQuantidade de saques restantes: \t{limite_saques - numero_saques}"
        )

    return saldo, extrato

def depositar(saldo, valor, extrato, operacao, /):
    if valor <= 0:
        print("O valor a ser depositado deve ser positivo")

    elif valor > 0:
        saldo += valor
        operacao += 1
        mensagem_extrato = f"\nOperação 00{operacao}:\n\t{'Tipo da Operação:':<{25}}[1] Depósito \n\t{'Valor da Operação:':<{25}}R$ +{valor:.2f} \n\t{'Saldo Após Operação:':<{25}}R$ {saldo:.2f}\n"
        extrato += mensagem_extrato

        print(
            f"A quantia de R$ {valor:.2f} foi depositada em sua conta. \nSaldo atual: R$ {saldo:.2f}"
        )
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("==================== EXTRATO ====================")

    historico = [print(op, end="") for op in extrato]

    print(f"\nSaldo atual: R$ {saldo:.2f}\n")
    print("=================================================")

    return historico

def criar_usuario(usuarios, /):
    """
    Usuários são armazenados em uma lista chamada 'usuarios'
    Endereço é string no formado Rua, Nº, Bairro, cidade, UF
    CPF deve ser armazenado no formato de somente numeros
    Não é possivel cadastrar dois usuarios ao mesmo tempo
    """
    cpf = int(input("\tCPF (Somente números): "))
    checar_usuario = filtrar_usuario(cpf, usuarios)
    
    #Se o usuário existir, não deixa duplicar
    if checar_usuario:
        print("\tUsuário ja existe!")
        return
    
    usuario = dict(
        cpf=cpf,
        nome=str(input("\tNome: ")),
        data_nascimento=str(input("\tData de Nascimento (dd-mm-aaaa): ")),
        endereco=str(input("\tEndereço (Rua, Nº, Bairro, cidade, UF): ")),
    )

    # Adiciona o novo usuário se ele não existir
    usuarios.append(usuario)

    print("\tUsuário criado com sucesso!")

def listar_usuarios(usuarios, contas, /, *, agencia):
    print("\t==================== CLIENTES ====================")
    print(f"\tTotal de Clientes: \t{len(usuarios)}")

    for i in range(len(usuarios)):
        print(f"\n\tNome: \t{usuarios[i]['nome']}")
        print(f"\tData de Nascimento: \t{usuarios[i]['data_nascimento']}")
        print(f"\tCPF: \t{usuarios[i]['cpf']}")
        print(f"\tEndereço: \t{usuarios[i]['endereco']}")

        print("=================================================")

    return

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados =  [u for u in usuarios if u['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta_corrente(agencia, numero_conta, usuarios, /):
    """
    Contas são armazenadas em uma lista chamada 'contas'
    É composta por agencia, n da conta e usuario;
    Número da conta é sequencial, iniciando em 1;
    Número da agencia é fixo, sendo '0001' - definido na const 'NUMERO_AGENCIA' em 'settings.py'
    Usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário
    """
    cpf = int(input("\tCPF (Somente números): "))
    checar_usuario = filtrar_usuario(cpf, usuarios)
    
    conta = dict(
        usuario=checar_usuario,
        agencia=agencia,
        numero_da_conta=numero_conta
    )    
    #Se o usuário existir, permite a criação de conta
    if checar_usuario:
        print(f"\tConta Corrente criada! \n\tO número da sua conta é:\t{conta["numero_da_conta"]}")
        return conta
    
    # Se o usuário não for cadastrado, não deixa criar a conta
    print("\tCPF inexistente. Crie um usuário para criar uma conta corrente.")

def listar_contas(contas):
    for i in range(len(contas)):
        print(f"\n\tAgência: \t{contas[i]['agencia']}")
        print(f"\tC/C: \t{contas[i]['numero_da_conta']}")
        print(f"\tTitular: \t{contas[i]['usuario']['nome']}")
        print("=================================================")        
        
def main():
    LIMITE_SAQUES = 3
    NUMERO_AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    operacao = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()  # Chama a função menu() para imprimir o menu

        if opcao == 0:  # sair do sistema
            print("Obrigado por utilizar nossos serviços. Volte sempre!")
            break

        # Chama a função depositar() passando o valor a ser depositado
        elif opcao == 1:
            valor = float(input("Quanto você gostaria de depositar? "))
            saldo, extrato = depositar(saldo, valor, extrato, operacao)

        # Chama a função sacar() passando o valor a ser sacado
        elif opcao == 2:
            print("\t[2] Saque Selecionado")
            valor = int(input("Informe o valor desejado para saque: R$"))
            sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                operacao=operacao,
            )

        # Exibe extrato pela função exibir_extrato()
        elif opcao == 3:
            print("\t[3] Extrato Selecionado.")
            exibir_extrato(saldo, extrato=extrato)

        # Chama a função criar_conta_corrente()
        elif opcao == 4:
            numero_conta = len(contas) + 1
            print("\t[4] Criar Conta Selecionado.")
            conta = criar_conta_corrente(NUMERO_AGENCIA, numero_conta, usuarios)

            if conta :
                contas.append(conta)
        
        elif opcao == 5:
            print("\t[5] Listar Contas Selecionado.")
            listar_contas(contas)
                
        # Chama a função criar_usuario()
        elif opcao == 6:
            print("\t[6] Criar Usuário Selecionado.")
            criar_usuario(usuarios)

        # Chama a função listar_usuarios()
        elif opcao == 7:
            print("\t[7] Listar Usuários Selecionado.")
            listar_usuarios(usuarios, contas, agencia=NUMERO_AGENCIA)

        else:
            print("\tOperação inválida! Por favor, selecione a operação desejada.")
    return


main()
