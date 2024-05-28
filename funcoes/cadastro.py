from funcoes import conect_banco

con = conect_banco.ConexaoBanco()


def criartabinvests():
    """Criar tabela de investimentos no banco de dados"""
    sqlcriartb = (f"CREATE TABLE investimentos (ID_INVEST INTEGER "
                  f"PRIMARY KEY AUTOINCREMENT,"
                  f"NOME VARCHAR(50),DATAINI "
                  f"DATE,DATARESG DATE, VALORini "
                  f"DECIMAL(6, 2),CUSTODIA VARCHAR(40), ENCERRADO BOOLEAN);")
    try:
        c = con.cursor()
        c.execute(sqlcriartb)
        con.commit()
        print("Tabela criada!") # >>>>>> APAGAR PRINT
    except con.Error as ex:
        print(ex) # >>>>>> APAGAR PRINT
class Cadastro:
    def __init__(self, instit,tipo, index,taxa, datini, datres ,valor,nin,custodia):
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
        self.custodia = custodia

    def criartab(self):
        """Criar tabela de investimento no banco de dados"""
        sqlcriartb = (f"CREATE TABLE '{self.ident}' (ID_MES INTEGER PRIMARY "
                      f"KEY AUTOINCREMENT, MES VARCHAR(4),"
                      f"ANO VARCHAR(4),VALOR DECIMAL(6, 2),RENDIMENTO DECIMAL(5, 2),TAXA DECIMAL(3, 2));")
        try:
            c = con.cursor()
            c.execute(sqlcriartb)
            con.commit()
            print("Tabela criada!") # >>>>>> APAGAR PRINT
        except con.Error as ex:
            print(ex) # >>>>>> APAGAR PRINT

    def inseririnvest(self):
        """Inserir dados"""
        sqlinserir = (
            f"INSERT INTO investimentos(NOME,DATAINI, "
            f"DATARESG, VALORini,CUSTODIA, ENCERRADO) "
            f"VALUES('{self.nome}', '{self.ini}', '{self.res}', "
            f"'{self.valor}','{self.custodia}', False);")

        try:
            c = con.cursor()
            c.execute(sqlinserir)
            con.commit()
            print("Dados inseridos!") # >>>>>> APAGAR PRINT
        except con.Error as ex:
            print(ex) # >>>>>> APAGAR PRINT


