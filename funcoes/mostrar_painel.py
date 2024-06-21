from funcoes import conect_banco
#Pega as informações do Banco de dados, para a apresentação em forma de painel
conexao = conect_banco.ConexaoBanco()
cursor = conexao.cursor()

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Aug", "Set","Out",
             "Nov", "Dez"]

def construir_painel(ano):
    """Consultar dados"""

    painel, taxas, rendimentos,valores = [], [], [], []

    sql = "SELECT CODIGO FROM investimentos"
    c = conexao.cursor()
    c.execute(sql)
    invests = [row[0] for row in c.fetchall()]
    nomes = list()
    for n in invests:
        nomes.append(n)
    print(nomes)
    for m in  meses:
        val = 0
        rend = 0
        for n in nomes:
            sql2 = (f"SELECT VALOR FROM '{n}' WHERE MES = '{m}' AND ANO = "
                    f"'{ano}'")
            c.execute(sql2)
            try:
                valor = c.fetchone()[0]
            except:
                valor = 0
            else:
                val += valor
                print(val)
            sql3 = (f"SELECT RENDIMENTO FROM '{n}' WHERE MES = '{m}' AND ANO = "
                    f"'{ano}'")
            c.execute(sql3)
            try:
                redimento = c.fetchone()[0]
            except:
                redimento = 0
            else:
                rend += redimento
                print(rend)
        valores.append(val)
        rendimentos.append(rend)
    for val in valores:
        if val > 0:
            n = valores.index(val)
            taxa = (rendimentos[n]/val)*100
            taxas.append(round(taxa,3))
        else:
            taxa = 0
            taxas.append(taxa)
    painel.append(valores.copy())
    painel.append(rendimentos.copy())
    painel.append(taxas.copy())
    print(painel)

    return painel


