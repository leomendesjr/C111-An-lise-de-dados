from cProfile import label
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

space = pd.read_csv("space.csv", delimiter=";", index_col = 0)
paises = pd.read_csv("paises.csv", delimiter=";")

# 1) Quantas empresas dos EUA e da China???
eua = len(space.loc[space["Location"].str.contains("USA"), "Company Name"].unique())
china = len(space.loc[space["Location"].str.contains("China"), "Company Name"].unique())

plt.figure(figsize = (12,8))

plt.title("Companhias espaciais EUA x China")

plt.bar(x = [0,1], height = [eua, china], color = ["#030b99", "#8c0404"])

plt.ylabel("# de companhias")
plt.xlabel("Países")

plt.xticks(ticks=[0,1], labels=["EUA", "China"])

plt.show()


# 2) Taxa de mortalidade e natalidade na américa do norte

n_america = paises.loc[paises["Region"].str.contains("NORTHERN AMERICA"), ["Country", "Birthrate", "Deathrate"]]

plt.figure(figsize = (12,8))

plt.title("Natalidade x Mortalidade nos países da América do Norte")

plt.plot(np.arange(len(n_america)), n_america["Birthrate"], color = "green", marker= "o", linestyle = "-", label = "Natalidade")
plt.plot(np.arange(len(n_america)), n_america["Deathrate"], color = "red", marker= "o", linestyle = "-", label = "Mortalidade")

plt.xticks(ticks = np.arange(len(n_america)), labels=n_america["Country"])
plt.xlabel("Países")
plt.ylabel("Taxa de Natalidade/Mortalidade")

plt.legend()

plt.show()