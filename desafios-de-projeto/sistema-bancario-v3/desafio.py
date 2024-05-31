import textwrap
from abc import ABC, abstractmethod
from datetime import datetime



class Cliente:
    endereco: str
    contas: list
    
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    cpf: str
    nome: str
    data_nascimento: datetime
    
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
       
class Conta:
    #anotação de tipo
    saldo: float
    numero: int
    agencia: str
    cliente: Cliente
    historico = Historico
    
    def __init__(self, cliente, numero):
        #Atributos definidos anteriormente no desafio e que deveriam ter esses valores iniciais
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)        
    
    @property
    def saldo(self, valor):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
 
        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False    
            
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

class ContaCorrente(Conta):
    limite: float
    limite_saques: int
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        pass
               
class Historico:
    def adicionar_transacao(transacao: Transacao):
        pass  

class Transacao(ABC):
    
    @abstractmethod
    def registrar(conta: Conta)
    

class Deposito:
    valor: float
    def __init__(self, valor: float):
        self.valor = valor
        
class Saque:
    valor: float
    pass



