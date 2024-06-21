from funcoes import conect_banco
#Consulta/Inserção/Atualização

conexao = conect_banco.ConexaoBanco()
cursor = conexao.cursor()


def investsEncerrados():
    """Mostra os investimentos encerrados"""
    sql = "SELECT NOME FROM investimentos WHERE ENCERRADO = 1"
    c = conexao.cursor()
    c.execute(sql)
    resultado = [row[0] for row in c.fetchall()]
    return resultado

class Encerrar:
    def __init__(self, nome_invest):
        self.nome_invest = nome_invest

        cursor.execute(f"SELECT CODIGO FROM investimentos WHERE NOME = "
                       f"'{self.nome_invest}'")
        self.codigo = cursor.fetchone()[0]
        print(self.codigo)

    def encerrarInvest(self):
        """Encerrar investimento"""
        sqlinserir = (
            f"UPDATE investimentos SET ENCERRADO = True WHERE CODIGO = '{self.codigo}'")

        try:
            c = conexao.cursor()
            c.execute(sqlinserir)
            conexao.commit()
            print("Investimento encerrado!") # >>>>>> APAGAR PRINT
        except conexao.Error as ex:
            print(ex) # >>>>>> APAGAR PRINT