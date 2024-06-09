
# Desafio Decoradores, Iteradores e Geradores

**Objetivo**:

Implementar as seguintes funcionalidades no sistema bancário:

* Decorador de Log
* Gerador de Relatórios
* Iterador Personalizado

Alterar o [Código Original](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/03%20-%20Decoradores%2C%20Iteradores%20e%20Geradores/desafio/desafio_v1.py) implementando os conceitos aprendidos.


### Decorador de Log:
Implementar um decorador que seja aplicado a todas as funções de transações (depósito, saque, criação de conta etc).

Deve printar a **data e hora de cada transação**, bem como o **tipo de transação**.

### Gerador de Relatórios:
Criar um gerador que permita iterar sobre as transações de uma conta e retornar, uma a uma, transações que foram realizadas.

Também deve possuir uma forma de filtrar as transações baseado em seu tipo (exemplo: apenas saques ou apenas depósitos)

### Iterador Personalizado
Implementar um **iterador personalizado** ```ContaIterador``` que permita iterar sobre todas as contas do banco, retornando informações básicas de cada conta (número, saldo atual etc).
