# Importações de bibliotecas necessárias
import math
import random
import datetime
import statistics
import locale

# Definições de variáveis que precisamos (def)



# Entradas obrigatórias (utilizei def e mandei imprimir em seguida)
def capital_inicial():
    ci = int(input('Capital Inicial (R$): '))
    return ci

def aporte_mensal():
    am = int(input('Aporte Mensal (R$): '))
    return am

def prazo_meses():
    pm = int(input('Prazo (meses): '))
    return pm

def cdi_anual():
    ca = float(input('CDI Anual(%): '))
    return ca

def percentual_cdi_no_cdb():
    pcc = int(input('Percentual CDI no CDB (%): '))
    return pcc

def percentual_cdi_na_lci():
    pci = int(input('Percentual CDI na LCA (%): '))
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