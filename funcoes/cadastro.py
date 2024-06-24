from funcoes import conect_banco
import datetime as dt
#Criação de investimentos

con = conect_banco.ConexaoBanco()

def criartabinvests():
    """Criar tabela com todos os investimentos no banco de dados"""
    sqlcriartb = (f"CREATE TABLE investimentos (ID_INVEST INTEGER "
                  f"PRIMARY KEY AUTOINCREMENT,"
                  f"NOME VARCHAR(50),DATAINI "
                  f"DATE,NTIMEINI TIMESTAMP,DATARESG DATE,NTIMERES TIMESTAMP, VALORini "
                  f"DECIMAL(6, 2),CUSTODIA VARCHAR(40),CODIGO VARCHAR(5) ,"
                  f"ENCERRADO BOOLEAN);")
    try:
        c = con.cursor()
        c.execute(sqlcriartb)
        con.commit()
        print("Tabela criada!") # >>>>>> APAGAR PRINT
    except con.Error as ex:
        print(ex) # >>>>>> APAGAR PRINT
class Cadastro:
    def __init__(self, instit,tipo, index,taxa, datini, datres ,valor,custodia):
        self.instit = instit
        self.tipo = tipo
        self.index = index
        self.taxa = taxa
        self.ini = datini
        dtt = datini.split("/") #data inicial dividida
        self.ntimeini = dt.datetime.timestamp(dt.datetime(int(dtt[2]), int(dtt[1]), int(dtt[0]), 23, 59, 59))
        self.res = datres
        dttres = datini.split("/")#data de resgate dividida
        self.ntimeres = dt.datetime.timestamp(dt.datetime(int(dttres[2]), int(dttres[1]), int(dttres[0]), 23, 59, 59))
        self.valor = valor
        self.custodia = custodia

        #Criar idenficação e nome dos investimentos
        sqlcriartb = (f"SELECT COUNT(*) FROM investimentos")
        try:
            c = con.cursor()
            c.execute(sqlcriartb)
            self.nin = c.fetchone()[0] + 1
            self.nome = (f"{self.tipo} {self.taxa}% {self.instit}"
                         f" {self.res.replace('/', '.')}")
            self.ident = str(self.nin) + 'IN'
        except con.Error as ex:
            print(ex)  # >>>>>> APAGAR PRINT
    def criartab(self):
        """Criar tabela independente para cada investimento cadastrado na
        tabela investimentos"""
        sqlcriartb = (f"CREATE TABLE '{self.ident}' (ID_MES INTEGER PRIMARY "
                      f"KEY AUTOINCREMENT, MES VARCHAR(4),"
                      f"ANO VARCHAR(4),VALOR DECIMAL(6, 2),RENDIMENTO DECIMAL(5, 2),TAXA DECIMAL(3, 2), NTIME TIMESTAMP);")
        try:
            c = con.cursor()
            c.execute(sqlcriartb)
            con.commit()
            print("Tabela criada10!") # >>>>>> APAGAR PRINT
        except con.Error as ex:
            print(ex) # >>>>>> APAGAR PRINT


    def inseririnvest(self):
        """Inserir dados"""
        print(self.ident)
        print(type(self.ident))
        sqlinserir = (
            f"INSERT INTO investimentos(NOME,DATAINI,NTIMEINI, "
            f"DATARESG, NTIMERES, VALORini,CUSTODIA, CODIGO, ENCERRADO) "
            f"VALUES('{self.nome}', '{self.ini}','{self.ntimeini}', '{self.res}','{self.ntimeres}',  "
            f"'{self.valor}','{self.custodia}','{self.ident}', False);")

        try:
            c = con.cursor()
            c.execute(sqlinserir)
            con.commit()
            print("Dados inseridos!") # >>>>>> APAGAR PRINT
        except con.Error as ex:
            print(ex) # >>>>>> APAGAR PRINT
