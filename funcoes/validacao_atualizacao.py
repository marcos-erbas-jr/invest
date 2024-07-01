from funcoes import atualizar
from funcoes import conect_banco
import datetime as dt
from informacoes import filtros_calendario as fc


#Verifica se o timestamp da Atualização é maior que o timestamp inicial

conexao = conect_banco.ConexaoBanco()
cursor = conexao.cursor()

class Validar:
    def __init__(self, mes, valor, nome_invest, ano):
        self.nome_invest = nome_invest
        self.mes = mes
        self.valor = float(valor)
        self.ano = ano
        self.nome_invest = nome_invest
        self.timestamp = (dt.datetime.timestamp(dt.datetime(int(ano), fc.meses.index(mes) + 1, 21, 23, 59, 59)))
        # self.timestamp gera o timestamp de um investimento cadastrado às 23h:59m:59s do dia 21 do mês e ano informado

        cursor.execute(f"SELECT CODIGO FROM investimentos WHERE NOME = "
                       f"'{self.nome_invest}'")
        print(self.nome_invest)
        self.codigo = cursor.fetchone()[0]

        cursor.execute(f"SELECT NTIMEINI FROM investimentos WHERE NOME = "
                       f"'{self.nome_invest}'")
        self.ntimeini = cursor.fetchone()[0]
        print(self.ntimeini)

        cursor.execute(f"SELECT NTIMERES FROM investimentos WHERE NOME = "
                       f"'{self.nome_invest}'")
        self.ntimeres = cursor.fetchone()[0]
        print(self.ntimeres)

    def validacao(self):
        if self.timestamp > self.ntimeini and self.timestamp < self.ntimeres:
           salvar = atualizar.Atualizar(self.mes, self.valor, self.nome_invest, self.ano)
           salvar.calcular()
           salvar.inserirInvest()
           print("salvou")
        elif self.timestamp > self.ntimeres:
           return 2
        else:
            return 1
