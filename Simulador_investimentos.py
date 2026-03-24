# Importações de bibliotecas necessárias
import math
import random
import datetime
import statistics
import locale

# Definições de variáveis que precisamos (def)



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
    ca = float(input('CDI Anual(%): '))
    return ca

def percentual_cdi_no_cdb():
    pcc = int(input('Percentual CDI no CDB (%): '))
    return pcc

def percentual_cdi_na_lci():
    pci = int(input('Percentual CDI na LCI (%): '))
    return pci

def rentabilidade_fii():
    rfii = float(input('Rentabilidade FII (%): '))
    return rfii

def meta_financeira():
    mf = int(input('Meta Financeira (R$): '))
    return mf


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
#restante