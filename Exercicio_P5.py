import pandas as pd
import numpy as np

# Carregando DataSet
dfPaises = pd.read_csv('paises.csv',delimiter=';')

#Questão 01:
#A
paisesOceania = dfPaises['Country'][dfPaises['Region'].str.contains('OCEANIA')]
print('Paises da Oceania são:')
print(paisesOceania)
#B
print('O dataset possui ',len(paisesOceania),'paises da Oceania')

#Questão 02:
print('Taxa média de Alfabetização(Literacy (%)):',np.mean(dfPaises['Literacy (%)']), '%')

#Questão 03:
dfCRP = dfPaises[['Country','Region','Population']]
maxPopulation = dfCRP['Population'].max()
print('Nome e Região do país com maior população:', dfCRP[dfCRP['Population']==maxPopulation])

#Questão 04:
dfCC = dfPaises[['Country','Coastline (coast/area ratio)']]
dfCC[dfCC['Coastline (coast/area ratio)']==0].to_csv('noCoast.csv',sep=';',header=False)
print('Paises sem costa marítima guardado no arquivo (noCoast)')

