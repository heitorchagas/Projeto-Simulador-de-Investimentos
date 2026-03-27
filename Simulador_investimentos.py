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
    mes0 = hoje.month + pm
    ano = hoje.year + (pm - 1) // 12
    mes1 = (mes0 - 1) % 12 + 1
    return date(ano, mes1, hoje.day).strftime('%d/%m/%Y')


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
            print('Digita um valor válido')

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
            rfii = int(input('Rentabilidade (%): '))
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
    total_investido = totalInvestido(capital, aporte, meses)
    montante = total_investido * math.pow(1 + taxa_mensal, meses)
    lucro = montante - total_investido
    aliquota = calcular_aliquota(meses)
    imposto = lucro * aliquota
    valor_liq = montante - imposto
    return valor_liq
    
# Calcular LCI
def lci(capital, aporte, meses, ca, pci):
    taxa_mensal = CDIanualMensal(ca) * (pci / 100)
    total_investido = totalInvestido(capital, aporte, meses)
    montante = total_investido * math.pow(1 + taxa_mensal, meses)
    return montante
    
# Calcular poupança
def poupanca(capital, aporte, meses):
    taxa_mensal = 0.005
    total_investido = totalInvestido(capital, aporte, meses)
    montante = total_investido * math.pow(1 + taxa_mensal, meses)
    return montante
    
# Calcular FII com a simulação
def calcular_fii(capital, aporte, meses, rfii):
    taxa_mensal = rfii / 100
    total_investido = totalInvestido(capital, aporte, meses)
    
    # 5 simulações independentes
    sim1 = total_investido * math.pow(1 + taxa_mensal, meses) * (1 + random.uniform(-0.03, 0.03))
    sim2 = total_investido * math.pow(1 + taxa_mensal, meses) * (1 + random.uniform(-0.03, 0.03))
    sim3 = total_investido * math.pow(1 + taxa_mensal, meses) * (1 + random.uniform(-0.03, 0.03))
    sim4 = total_investido * math.pow(1 + taxa_mensal, meses) * (1 + random.uniform(-0.03, 0.03))
    sim5 = total_investido * math.pow(1 + taxa_mensal, meses) * (1 + random.uniform(-0.03, 0.03))
    
    simulacoes = [sim1, sim2, sim3, sim4, sim5]
    
    media = statistics.mean(simulacoes)
    mediana = statistics.median(simulacoes)
    desvio = statistics.stdev(simulacoes)
    
    return media, mediana, desvio

print('---' * 12)
ci = capital_inicial()
am = aporte_mensal()
pm = prazo_meses()
ca = cdi_anual()
pcc = percentual_cdi_no_cdb()
pci = percentual_cdi_na_lci()
rfii = rentabilidade_fii()
mf = meta_financeira()
print('---' * 12)

# Impressão do relatório

    # data do relatório pyinvest
data_relatorio = relatorio_data()
print(f'Data do relatório - {data_relatorio}')
resgate = data_estimada(pm)
print(f'Data estimada de resgate: {resgate}')