from funcoes import conect_banco
#Consulta/Inserção/Atualização

conexao = conect_banco.ConexaoBanco()
cursor = conexao.cursor()

def consultaCodigo():
    """Consultar dados"""
    sql = "SELECT CODIGO FROM investimentos"
    c = conexao.cursor()
    c.execute(sql)
    resultado = [row[0] for row in c.fetchall()]
    return resultado

def consultaNome():
    """Consultar dados"""
    sql = "SELECT NOME FROM investimentos WHERE ENCERRADO = 0"
    c = conexao.cursor()
    c.execute(sql)
    resultado = [row[0] for row in c.fetchall()]
    return resultado

class Atualizar:
    def __init__(self, mes,valor, nome_invest, ano):
        self.nome_invest = nome_invest
        self.mes = mes
        self.valor = float(valor)
        self.ano = ano

        cursor.execute(f"SELECT CODIGO FROM investimentos WHERE NOME = "
                       f"'{self.nome_invest}'")
        self.codigo = cursor.fetchone()[0]
        print(self.codigo)

    def calcular(self):
        """Função utilizada para calcular o valor do redimento e a taxa do
        mês"""

        cursor.execute(f"SELECT COUNT(*) FROM '{self.codigo}'")

        # Obtém o resultado da consulta
        num_registros = cursor.fetchone()[0]

        # Verifica se a tabela tem registros
        if num_registros > 0:
            print("A tabela tem registros.") # >>>>>> APAGAR PRINT
            cursor.execute(
                f"SELECT ID_MES FROM '{self.codigo}' ORDER BY ID_MES DESC "
                f"LIMIT 1")

            # Obtém o resultado da consulta
            ultimo_id = cursor.fetchone()[0]

            cursor.execute(f"SELECT VALOR FROM '{self.codigo}' WHERE "
                         f"ID_MES = "
                            f"?",(ultimo_id,))

            ultimo_valor = float(cursor.fetchone()[0])

            self.redimento = self.valor - ultimo_valor
            self.taxa = round((self.redimento / ultimo_valor)*100, 3) #round
            # arredonda a taxa mensal para 3 casas
        else:
            cursor.execute(f"SELECT VALORini FROM investimentos WHERE CODIGO = "
                            f"'{self.codigo}'")
            valor_ini = float(cursor.fetchone()[0])

            self.redimento = self.valor - valor_ini
            self.taxa =round((self.redimento / valor_ini)*100, 3)



    def inserirInvest(self):
        """Inserir dados"""
        sqlinserir = (
            f"INSERT INTO '{self.codigo}'(MES,VALOR, "
            f"RENDIMENTO, TAXA, ANO) "
            f"VALUES('{self.mes}', '{self.valor}', '{self.redimento}', "
            f"'{self.taxa}', '{self.ano}');")

        try:
            c = conexao.cursor()
            c.execute(sqlinserir)
            conexao.commit()
            print("Dados inseridos!") # >>>>>> APAGAR PRINT
        except conexao.Error as ex:
            print(ex) # >>>>>> APAGAR PRINT