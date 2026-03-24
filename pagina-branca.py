# Importações de bibliotecas necessárias
import math
import random
import datetime
import statistics
import locale

# Definições de variáveis (def)



# Entradas obrigatórias
def capital_inicial():
    int(input('Capital Inicial (R$): '))

def aporte_mensal():
    int(input('Aporte Mensal (R$): '))

def prazo_meses():
    int(input('Prazo (meses): '))

def cdi_anual():
    float(input('CDI Anual(%): '))

def percentual_cdi_no_cdb():
    int(input('Percentual CDI no CDB (%): '))

def percentual_cdi_na_lci():
    int(input('Percentual CDI na LCA (%): '))

def rentabilidade_fii():
    float(input('Rentabilidade FII (%): '))

def meta_financeira():
    int(input('Meta Financeira (R$): '))