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