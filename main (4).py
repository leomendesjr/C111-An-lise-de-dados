# Exercícios Propostos - Cap05
# Author: Daniel Jardim Nunes - GEC - 1525
# Teacher: Renzo - C111

import numpy as np
import pandas as pd


'''Questão 01:'''
# Carregando DataSet
dfPaises = pd.read_csv('paises.csv',delimiter=';')

# A)- Países da OCEANIA
dfCR = dfPaises[['Country','Region']]
print(f"Países da OCEANIA:\n{dfCR[dfCR['Region'].str.contains('OCEANIA')]}\n")

# B)- Quantos países são da OCEANIA
print(f"Quantos países são da OCEANIA: {len(dfCR[dfCR['Region'].str.contains('OCEANIA')])} Países\n")

'''Questão 02'''
# Mostre a média da taxa de alfabetização(Literacy (%)) do Planeta
print(f"Taxa média de Alfabetização(Literacy (%)): {np.mean(dfPaises['Literacy (%)'])} %\n")

'''Questão 03'''
# Encontre o nome e a região do país que possui a maior população
dfCRP = dfPaises[['Country','Region','Population']]
maxPopulation = dfCRP['Population'].max()
print(f"Nome e Região do país com maior população:\n {dfCRP[dfCRP['Population']==maxPopulation]} \n")

'''Questão 04'''
# Busque o nome de todos os países que não possuem costa marítima(Coastline (coast/area ratio))
dfCC = dfPaises[['Country','Coastline (coast/area ratio)']]
dfCC[dfCC['Coastline (coast/area ratio)']==0].to_csv('noCoast.csv',sep=';',header=False)
print(f"Guardado com sucesso o nome de todos os países que não possuem costa marítima no novo arquivo chamado (noCoast.csv) :)\n")