# Importações de bibliotecas necessárias
import math
import random
import datetime
from datetime import date
import statistics
import locale

# Definições de variáveis que precisamos (def)

def relatorio_data():
    data = datetime.date.today()
    return data.strftime('%d/%m/%Y')
def data_estimada(pm):
    hoje = date.today()
    dias = pm * 30
    resgate = hoje + datetime.timedelta(days=dias)
    return resgate.strftime('%d/%m/%Y')


# Entradas obrigatórias (utilizei def e mandei imprimir em seguida)
def capital_inicial():
    while True:
        try:
            ci = int(input('Capital Inicial (R$): '))
            if ci < 0:
                print('insira um valor positivo')
                continue
            return ci
        except ValueError:
            print('Insira um valor válido')

def aporte_mensal():
    while True:
        try:
            am = int(input('Aporte Mensal (R$): '))
            if am < 0:
                print('Insira um valor positivo')
                continue
            return am
        except ValueError:
            print('Insira um valor válido')

def prazo_meses():
    while True:
        try:
            pm = int(input('Prazo (meses): '))
            if pm < 0:
                print('Insira um valor positivo')
                continue
            return pm
        except ValueError:
            print('Insira um valor válido')

def cdi_anual():
    while True:
        try:
            ca = float(input('CDI Anual(%): '))
            if ca < 0:
                print('Insira um valor positivo')
                continue
            return ca
        except ValueError:
            print('Insira um valor válido')

def percentual_cdi_no_cdb():
    while True:
        try:
            pcc = int(input('Percentual CDI no CDB (%): '))
            if pcc < 0:
                print('Insira um valor positivo')
                continue
            return pcc
        except ValueError:
            print('Insira um valor válido')
    

def percentual_cdi_na_lci():
    while True:
        try:
            pci = int(input('Percentual CDI na LCI (%): '))
            if pci < 0:
                print('Insira um valor positivo')
                continue
            return pci
        except ValueError:
            print('Insira um valor válido')

def rentabilidade_fii():
    while True:
        try:
            rfii = float(input('Rentabilidade FII (%): '))
            if rfii < 0:
                print('Insira um valor positivo')
                continue
            return rfii
        except ValueError:
            print('Insira um valor válido')

def meta_financeira():
    while True:
        try:
            mf = int(input('Meta Financeira (R$): '))
            if mf < 0:
                print('Insira um valor positivo')
                continue
            return mf
        except ValueError:
            print('Insira um valor válido')


#------------- Cálculos ---------------

# Convertendo CDI anual para mensal
def CDIanualMensal(ca):
    cm = math.pow(1 + ca / 100, 1 / 12) - 1
    return cm

# Calculando o total investido
def totalInvestido(capital, aporte, meses):
    total_Investido = capital + (aporte * meses)
    return total_Investido

# Calcular os dias
def calcular_aliquota(meses):
    dias = meses * 30
    if dias <= 180:
        return 0.225
    
    elif dias <= 360:
        return 0.2
    
    elif dias <= 720:
        return 0.175
    
    else:
        return 0.15

# Calcular CDB
def cdb(capital, aporte, meses, ca, pcc):
    taxa_mensal = CDIanualMensal(ca) * (pcc / 100)
    montante = capital * math.pow(1 + taxa_mensal, meses) + aporte * (math.pow(1 + taxa_mensal, meses) - 1) / taxa_mensal
    total_investido = totalInvestido(capital, aporte, meses)
    lucro = montante - total_investido
    aliquota = calcular_aliquota(meses)
    imposto = lucro * aliquota
    valor_liq = montante - imposto
    return valor_liq
    
# Calcular LCI
def lci(capital, aporte, meses, ca, pci):
    taxa_mensal = CDIanualMensal(ca) * (pci / 100)
    montante = capital * math.pow(1 + taxa_mensal, meses) + aporte * (math.pow(1 + taxa_mensal, meses) - 1) / taxa_mensal
    return montante
    
# Calcular poupança
def poupanca(capital, aporte, meses):
    taxa_mensal = 0.005
    montante = capital * math.pow(1 + taxa_mensal, meses) + aporte * (math.pow(1 + taxa_mensal, meses) - 1) / taxa_mensal
    return montante
    
# Calcular FII com a simulação
def calcular_fii(capital, aporte, meses, rfii):
    taxa_mensal = rfii / 100
    base = capital * math.pow(1 + taxa_mensal, meses) + aporte * (math.pow(1 + taxa_mensal, meses) - 1) / taxa_mensal
    
    # 5 simulações independentes
    sim1 = base * (1 + random.uniform(-0.03, 0.03))
    sim2 = base * (1 + random.uniform(-0.03, 0.03))
    sim3 = base * (1 + random.uniform(-0.03, 0.03))
    sim4 = base * (1 + random.uniform(-0.03, 0.03))
    sim5 = base * (1 + random.uniform(-0.03, 0.03))
    
    simulacoes = [sim1, sim2, sim3, sim4, sim5]
    
    media = statistics.mean(simulacoes)
    mediana = statistics.median(simulacoes)
    desvio = statistics.stdev(simulacoes)
    
    return media, mediana, desvio

# Definir o tamanho da barra
def barra(valor, maior):
    tamanho = int((valor / maior) * 50)
    return '█' * tamanho

# Função principal
def main():
    print('==' * 12, 'SIMULADOR DE INVESTIMENTOS - PYINVEST', '==' * 12)
    ci = capital_inicial()
    am = aporte_mensal()
    pm = prazo_meses()
    ca = cdi_anual()
    pcc = percentual_cdi_no_cdb()
    pci = percentual_cdi_na_lci()
    rfii = rentabilidade_fii()
    mf = meta_financeira()
    total_inv = totalInvestido(ci, am, pm)
    valor_cdb = cdb(ci, am, pm, ca, pcc)
    valor_lci = lci(ci, am, pm, ca, pci)
    valor_poup = poupanca(ci, am, pm)
    valor_fii, mediana_fii, desvio_fii = calcular_fii(ci, am, pm, rfii)

    gerar_relatorio(ci, am, pm, total_inv, valor_cdb, valor_lci, valor_poup, valor_fii, mediana_fii, desvio_fii, mf)

# Geração do relatório
def gerar_relatorio(ci, am, pm, total_inv, valor_cdb, valor_lci, valor_poup, valor_fii, mediana_fii, desvio_fii, mf):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    maior = max(valor_cdb, valor_lci, valor_poup, valor_fii)

    print('=' * 50)
    print(f'RELATÓRIO PYINVEST - {relatorio_data()}')
    print(f'Data estimada de resgate: {data_estimada(pm)}')
    print(f'Total investido: {locale.currency(total_inv, grouping=True)}')
    print('-' * 50)

    print(f'CDB      : {locale.currency(valor_cdb, grouping=True)}')
    print(f'Gráfico  : {barra(valor_cdb, maior)}')
    print(f'LCI/LCA  : {locale.currency(valor_lci, grouping=True)}')
    print(f'Gráfico  : {barra(valor_lci, maior)}')
    print(f'Poupança : {locale.currency(valor_poup, grouping=True)}')
    print(f'Gráfico  : {barra(valor_poup, maior)}')
    print(f'FII      : {locale.currency(valor_fii, grouping=True)}')
    print(f'Gráfico  : {barra(valor_fii, maior)}')
    print('-' * 50)

    print(f'Estatísticas FII (Mediana): {locale.currency(mediana_fii, grouping=True)}')
    print(f'Desvio Padrão FII: {locale.currency(desvio_fii, grouping=True)}')

    meta_atingida = 'Sim' if max(valor_cdb, valor_lci, valor_poup, valor_fii) >= mf else 'Não'
    print(f'Meta atingida? {meta_atingida}')

    melhor_valor = maior
    if melhor_valor == valor_cdb:
        melhor_final = 'CDB'

    elif melhor_valor == valor_lci:
        melhor_final = 'LCI/LCA'

    elif melhor_valor == valor_poup:
        melhor_final = 'Poupança'

    else:
        melhor_final = 'FII (Média)'
    
    print(f'\nMelhor opção: {melhor_final} com {locale.currency(melhor_valor, grouping=True)}')
    print('=' * 50)


if __name__ == '__main__': main()