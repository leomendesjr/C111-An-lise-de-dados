import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from cProfile import label

#Lendo os dataset
dfPaises = pd.read_csv('paises.csv', delimiter=';')
space = pd.read_csv('space.csv', delimiter=';')

#1
#Paises dos EUA
paisesEUA = len(space.loc[space['Location'].str.contains('USA'), 'Company Name'].unique())
print(paisesEUA)

#Paises da China
paisesChina = len(space.loc[space['Location'].str.contains('China'), 'Company Name'].unique())
print(paisesChina)

#Plotando gráfico em barras
plt.bar(x = [0,1], height = [paisesEUA, paisesChina], color = ["#030b99", "#8c0404"], edgecolor = ['white','yellow'], hatch = '*')

#Colocando legenda no gráfico
plt.title("Companhias")
plt.xlabel("Países")
plt.ylabel("Quant de companhias")
plt.xticks(ticks=[0,1], labels=["EUA", "China"])
plt.show()

#2
info_north = dfPaises.loc[dfPaises["Region"].str.contains("NORTHERN AMERICA"), ["Country", "Birthrate", "Deathrate"]]

#Printando as retas para Natalidade e mortalidade
plt.plot(np.arange(len(info_north)), info_north["Deathrate"], color = "black", marker= "*", linestyle = "-", label = "Mortalidade")
plt.plot(np.arange(len(info_north)), info_north["Birthrate"], color = "green", marker= "*", linestyle = "-", label = "Natalidade")

#Colocando legenda no gráfico
plt.title("Natalidade x Mortalidade")
plt.xticks(ticks = np.arange(len(info_north)), labels=info_north["Country"])

plt.xlabel("Paises")
plt.ylabel("Quantidade")
plt.legend()
plt.show()