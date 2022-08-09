import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Dados do Eixo X
x = np.array([1,2,3,4])
#Dados do Eixo Y1
y = x*2 #broadcasting
#Dados do Eixo Y2
y2 = x**2
'''
plt.xlabel('Dados do Eixo X')
plt.ylabel("Dados do Eixo Y")
plt.plot(x, y, '+:g', x, y2, 'b--', linewidth=3, markersize=20)
plt.show()


#Exemplo de subplot
plt.subplot(1,2,1)
plt.title('Linear')
plt.plot(x,y,'r-')

plt.subplot(1,2,2)
plt.title('Exponencial')
plt.plot(x,y2,'b--')

plt.show()
'''
#Exemplo com scatter plot
#Baixando o Dataset para um DataFrame
dfPaises = pd.read_csv('paises.csv', delimiter=';')
#pegando os 6 maiores paises do Dataset
dfPaises2 = dfPaises.nlargest(6, 'Area (sq. mi.)')

#tracando o grafico
#primeiro argumento - eixo x
#segundo argumento - eixo y
#terceiro argumento - tamanho bolinha
plt.scatter(dfPaises2['Country'], dfPaises2['GDP ($ per capita)'], s=dfPaises2['Area (sq. mi.)']/10000)
plt.show()

