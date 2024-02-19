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
class Cadastro:
    def __init__(self, instit,tipo, index,taxa, datini, datres ,valor,nin):
        self.instit = instit
        self.tipo = tipo
        self.index = index
        self.taxa = taxa
        self.ini = datini
        self.res = datres
        self.valor = valor
        self.nin = nin
        self.nome = (f"{self.nin}IN {self.tipo} {self.taxa}% {self.instit}"
                  f" {self.res.replace('/','.')}")
        self.ident = str(self.nin) + 'IN'

    def criartabinvests(self):
        """Criar tabela de investimentoS no banco de dados"""
        sqlcriartb = (f"CREATE TABLE investimentos (ID_INVEST INTEGER "
                      f"PRIMARY KEY AUTOINCREMENT,"
                      f"NOME VARCHAR(50),DATAINI "
                     f"DATE,DATARESG DATE, VALORini "
                     f"DECIMAL(6, 2), ENCERRADO BOOLEAN);")
        try:
            c = ConexaoBanco().cursor()
            c.execute(sqlcriartb)
            ConexaoBanco().commit()
            print("Tabela criada!")
        except Error as ex:
            print(ex)

    def criartab(self):
        """Criar tabela de investimento no banco de dados"""
        sqlcriartb = (f"CREATE TABLE '{self.ident}' (ID_MES INTEGER "
                      f"PRIMARY KEY AUTOINCREMENT, MES VARCHAR(4),"
                      f"VALOR DECIMAL(6, 2),RENDIMENTO DECIMAL(5, 2),"
                     f"TAXA DECIMAL(3, 2));")
        try:
            c = ConexaoBanco().cursor()
            c.execute(sqlcriartb)
            ConexaoBanco().commit()
            print("Tabela criada!")
        except Error as ex:
            print(ex)

    def inseririnvest(self):
        """Inserir dados"""
        sqlinserir = (
            f"INSERT INTO investimentos(NOME,DATAINI, "
            f"DATARESG, VALORini, ENCERRADO) "
            f"VALUES('{self.nome}', '{self.ini}', '{self.res}', "
            f"'{self.valor}', False);")

        try:
            con = ConexaoBanco()
            c = con.cursor()
            c.execute(sqlinserir)
            con.commit()
            print("Dados inseridos!")
        except Error as ex:
            print(ex)


C = Cadastro("Master", "CDB", "CDI", "12,05", "19/02/2024", "28/12/2030","1356,56","01" )
C.criartabinvests()
#C.inserir()

