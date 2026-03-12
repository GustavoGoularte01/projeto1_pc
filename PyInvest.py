import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale,LC_ALL, 'pt_BR.UTF-8')
#Entregas
capital = float(input('capital inicial: '))
aporte = float(input('Aporte mensal: '))
meses = float(input('CDI mensal: '))
cdi_anual = float(input('CDI anual %: '))
perc_cdb = float(input('percentual do CDI - CDB (%): '))/100
perc_lci = float(input('percentual do CDI - LCI (%): '))/100
taxa_fii = float(input('rentabilidade do FII: (%)'))/100
meta = float(input('meta financeira (R$): '))

#converção
cdi_mensal = math.pow((1+cdi_anual),1/12) -1
#total invesitido
total_investido = capital + (aporte*meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1+taxa_cdb),meses))+(aporte * meses)
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#lci/LCi
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci,meses))+(aporte * meses))

#poupança
taxa_poupanca = 0.005
montante_popanca = (capital* math,pow((1+taxa_poupanca),meses))+(aporte*meses)  

