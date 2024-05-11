def menu():
    menu = """
    ==================================== MENU PRINCIPAL ====================================

    Bem-vindo ao PyBank. Escolha a operação desejada

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Novo Usuário
    [6] Listar Usuários
    [0] Sair

    => """

    return int(input(menu))


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, operacao):
    saldo -= valor
    numero_saques += 1
    operacao += 1

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
            f"A quantia de R$ {valor} foi retirada da sua conta. \nSaldo atual: R$ {saldo:.2f}.\nQuantidade de saques restantes: {LIMITE_SAQUES - numero_saques}"
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

    usuario = dict(
        nome=str(input("Nome: ")),
        data_nascimento=str(input("Data de Nascimento: ")),
        cpf=int(input("CPF (Somente números): ")),
        endereco=str(input("Rua, Nº, Bairro, cidade, UF: ")),
        senha=str(input("Senha: ")),
    )

    # Verifica se   o usuário existe
    if usuario["cpf"] in [u["cpf"] for u in usuarios]:
        print("Usuário ja existe!")
        return

    # Adiciona o novo usuário se ele não existir
    usuarios.append(usuario)

    print("Usuário criado com sucesso!")


def listar_usuarios(usuarios, contas, /, *, agencia):
    print("==================== CLIENTES ====================")
    print(f"Total de Clientes: {len(usuarios)}")

    for i in range(len(usuarios)):
        print(f"\n Nome: {usuarios[i]['nome']}")
        print(f" Data de Nascimento: {usuarios[i]['data_nascimento']}")
        print(f" CPF: {usuarios[i]['cpf']}")
        print(f" Endereço: {usuarios[i]['endereco']}")

        print("=================================================")

    return


def criar_conta_corrente(contas, usuarios, /):
    """
    Contas são armazenadas em uma lista chamada 'contas'

    É composta por agencia, n da conta e usuario;

    Número da conta é sequencial, iniciando em 1;

    Número da agencia é fixo, sendo '0001' - definido na const 'NUMERO_AGENCIA' em 'settings.py'

    Usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário

    """

    conta = dict(
        numero_da_conta=contas[-1]["numero_da_conta"] + 1 if contas else 1,
        cpf_usuario=int(input("Digite seu CPF: ")),
    )

    # Checar se o CPF já existe (precisa ter um usuário criado para criar uma conta)
    if conta["cpf_usuario"] not in [u["cpf"] for u in usuarios]:
        print("CPF inexistente. Crie um usuário para criar uma conta corrente.")
        return

    # Se o usuário não tiver nenhuma conta, adiciona a nova conta normalmente
    contas.append(conta)
    print("Conta corrente criada!")

    contas.append(conta)
    return


def listar_contas():
    pass


# dica:
# para vincular um usuario a uma conta filtre a lista de usuario buscando pelo CPF informado para cada usuario da lista
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
            print("[2] Saque Selecionado")
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
            print("[3] Extrato Selecionado.")
            exibir_extrato(saldo, extrato=extrato)

        # Chama a função criar_conta_corrente()
        elif opcao == 4:
            print("[4] Criar Conta Selecionado.")
            criar_conta_corrente(contas, usuarios)

        # Chama a função criar_usuario()
        elif opcao == 5:
            print("[5] Criar Usuário Selecionado.")
            criar_usuario(usuarios)

        # Chama a função listar_usuarios()
        elif opcao == 6:
            print("[5] Listar Usuários Selecionado.")
            listar_usuarios(usuarios, contas, agencia=NUMERO_AGENCIA)

        else:
            print("Operação inválida! Por favor, selecione a operação desejada.")
    return


main()
