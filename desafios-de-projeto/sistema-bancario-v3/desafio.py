import textwrap
from abc import ABC, abstractmethod

class Deposito:
    valor: float
    pass

class Saque:
    valor: float
    pass

class Transacao(ABC):
    @abstractmethod
    def registrar(conta: Conta)

class Historico:
    def adicionar_transacao(transacao: Transacao)

class Cliente:
    endereco: str
    contas: list
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        pass
    
    def adicionar_conta(self, conta:Conta)

class PessoaFisica(Conta):
    cpf: str
    nome: str
    data_nascimento: date
    
class Conta:
    #anotação de tipo
    saldo: float
    numero: int
    agencia: str
    cliente: Cliente
    historico = Historico
    
    def saldo(self, valor:float) -> float:
        #deve retornar um float
        pass
    
    def nova_conta(self, cliente: Cliente, numero:int) -> 'Conta':
        #deve retornar o objeto Conta
        pass
    
    def sacar(self, valor: float) -> bool:
        #deve retornar um bool
        pass
    
    def depositar(self, valor: float) -> bool:
        #deve retornar um bool
        pass

class ContaCorrente(Conta):
    limite: float
    limite_saques: int
    pass


