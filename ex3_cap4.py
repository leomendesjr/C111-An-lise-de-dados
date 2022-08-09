import numpy as np

spaceDS = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')
#print(spaceDS)
#Vendo as colunas do dataset
#print(spaceDS[0])
#Vendo apenas o nome das empresas
#print(spaceDS[1:,1])
#Vendo apenas o nome das empresas sem repetições
#print(np.unique(spaceDS[1:,1]))
#print(np.unique(spaceDS[7:,7]))

# 1
quant_total = len(spaceDS[0:,0])-1
quant_success = len(np.where(spaceDS[:,7] == "Success")[0])
print("A porcentagem de sucesso é de ", (quant_success/quant_total)*100, "%")

#2
custo = spaceDS[1:, 6].astype(float)
custo = custo[custo > 0]
media_custo = np.sum(custo)/(quant_total-1)
print(f'A média dos custos das missões que tiveram gastos > 0: {round(media_custo,4)}')

#3
missoes = spaceDS[1:, 2].copy()
missoes_eua = np.char.find(missoes, 'USA')
missoes_eua = missoes_eua[missoes_eua != -1]
print(f'Números de lançamentos dos EUA:  {missoes_eua.size} ')

#4
empresas = spaceDS[:,1]
missao_spacex = spaceDS[empresas == "SpaceX"]
valores = missao_spacex[:,6]
spacex_missoes_caras = missao_spacex[valores == max(valores)]
print(f"Missões da SpaceX com maior valor = {max(valores)}\n{spacex_missoes_caras}")

#5
empresa, quantidade = np.unique(spaceDS[1:, 1], return_counts=True)
dicio = np.column_stack((empresa, quantidade)) 
print(f"Nomes das empresas | Quant de missoes\n {dicio}")