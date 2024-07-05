# **Explorando Banco de Dados Relacionais com DB API em Python**

## **Objetivo**
Abordar conceitos básicos de banco de dados relacional e como interagir com eles utilizando a DB API

### **O que é a DB API?**
É uma especificação que determina como o Python vai se comunicar com o SGBD (Sistema Gerenciador de Banco de Dados)

Praticamente funciona com qualquer DB. Simplesmente pesquise por "*python nome_sgbd connection*" no Google e deverá te retornar o driver a ser baixado.

Todos os drivers respeitam o mesmo método para conectar, alimentar etc por conta da [PEP249](https://peps.python.org/pep-0249/)

### **Criando um Banco de Dados**

```python
import sqlite3
conexao = sqlite3.connect("nome_do_banco.db")
``` 

### **Criando um Cursor**
Para poder executar comandos SQL, é necessário um cursor. Para isso, chame o método ``conexao.cursor()`` para estabelecê-lo.
```python
cursor = conexao.cursor()
```

A partir da cursão do cursor, é possível utilizar o método ``cursor.execute(sql_query)`` onde ``sql_query`` é seu comando SQL a ser executado.
```python
cursor.execute("SELECT * FROM clientes")
```

Para toda informação inserida e comando executado, é precisso '*comitar*' essas exeuções via ``conexao.commit()``


### **Consultando os Registros**
#### **Recuperando 1 registro**
O método ``cursor.fetchone()`` pode ser utilizado para recuperar 1 registro. Retorna o próximo registro na lista de resultados ou ``None``se não houver mais resultados.

```Python
cursor.execute("SELECT * FROM clientes WHERE id=1")
resultado = cursor.fetchone()
print(resultado)
```
#### **Recuperando Todos os Registros**
O método ``cursor.fetchall()`` pode ser utilizado para recuperar todos o registros de resultados de uma só vez. Retorna uma lista com os registros ou uma lista vazia se não houve resultados.
```Python
cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)
```

### **Utilizando row_factory**
Por padrão, resultados são retornados como **tuplas**. Utilizar row_factory permite uma organização melhor, posteriormente, para escrever códigos, uma vez que transforma a tupla em dicionários.
```Python
cursor.row_factory = sqlite3.Row
cursor.execute = ('SELECT * FROM clientes WHERE id=?;',(1,))
resultado = cursor.fetchone()
print(dict(resultado))
```
