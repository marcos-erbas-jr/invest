import sqlite3
from sqlite3 import Error
#Conectar ao banco de dados
def ConexaoBanco():
    """Método usado para realizar a conexão com o Banco de Dados, caso a
    conexão falhe, o método irá mostrar o erro. E se o banco não existir,
    será criado um dentro do diretorio"""
    caminho = "invest.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as er:
        print(er)
    return con

'''''''''# CFB Cursos - Aula 47 até 52- Python e Banco de Dados
#>>> Arquivo apenas para consulta da sintaxe SQL apagar este arquivo depois,
# pois não é necessário parao programa <<<<

import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    """Método usado para realizar a conexão com o Banco de Dados, caso a
    conexão falhe, o método irá mostrar o erro. E se o banco não existir,
    será criado um dentro do diretorio"""
    caminho = "invest.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as er:
        print(er)
    return con

vcon = ConexaoBanco()

#vsql recebe a query para criar a tabela
sql_criar_invest = """CREATE TABLE tb_contatos(
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(40)
            );"""

def criarTabela(conexao, sql):
    """Criar tabelas no banco de dados"""
    try:
        c = conexao.cursor()
        c.execute(sql)
        print("Tabela criada!")
    except Error as ex:
        print(ex)

vsql = """INSERT INTO tb_contatos 
            (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
            VALUES('teste_nome', '123456789', 'teste@gmail.com');"""
conexao = ConexaoBanco()
criarTabela(conexao, vsql)

def inserir(conexao, sql):
    """Inserir dados"""
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit() #commit() é usado para salvar a inserção, sem ele o
        # registro dá como inserido mas não aparece no banco de dados
        print("Dados inseridos!")
    except Error as ex:
        print(ex)

'Comando abaixo foi utilizado para criar a tabela tb_contatos'
#criarTabela(vcon, vsql)

'Comando abaixo foi utilizado para inserir dados em tb_contatos'
#inserir(vcon, vsql2)

"""'Inserido dados com a entrada do usuário'
nome = input('Digite seu nome: ')
tel = input("Digite seu telefone: ")
email = input('Digite seu e-mail: ')
vsql3 = (f"INSERT INTO tb_contatos(T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)VALUES('{nome}','{tel}','{email}');")
inserir(vcon, vsql3)"""

vsql4 = """DELETE FROM tb_contatos WHERE
            N_IDCONTATO=1;"""

def deletar(conexao, sql):
    """Deletar dados"""
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Dados deletados!")
    except Error as ex:
        print(ex)

'Comando abaixo foi utilizado para deletar dados em tb_contatos'
#deletar(vcon, vsql4)



vsql5 = """UPDATE tb_contatos SET T_NOMECONTATO='Bruno' WHERE
            N_IDCONTATO=1;"""
def atualizar(conexao, sql):
    """Atualizar dados"""
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Dados atualizado!")
    except Error as ex:
        print(ex)

'Comando abaixo foi utilizado para atualizar dados em tb_contatos'
#atualizar(vcon, vsql5)

'''
#vsql7 = """SELECT * FROM tb_contatos"""
#def consulta(conexao, sql):
"""Consultar dados"""
   # c = conexao.cursor()
   # c.execute(sql)
    #resultado = c.fetchall()
   # return resultado

'Comando abaixo foi utilizado para consultar dados em tb_contatos'
#res = consulta(vcon, vsql7)

#for resultados in res:
    #print(resultados)

#vcon.close()'''
