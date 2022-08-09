import numpy as np

# Carregando base de dados
data = np.loadtxt("space.csv", delimiter = ";", dtype = str, encoding="utf-8")
valid_data = data[1:,:] # Excluindo cabeçalho

# 1) Quantas missões deram certo (%)
total_missions = len(data)
status = valid_data[:,7]
success = len(status[status == "Success"])
print(f"Porcentagem de missões bem sucedidas {success *100 / len(status)} %")

# 2) Média de gastos de uma missão espacial se baseando em missões que possuam valores
# disponíveis (>0)
custo = valid_data[:, 6].astype(np.float)
missoes_com_custo = custo[custo > 0]
total_custos = np.sum(missoes_com_custo)
print(f"Custo médio de missões com custo > 0: {total_custos / len(missoes_com_custo)}")


# 3) Quantidade de missões realizadas pelos USA
locais = valid_data[:, 2]
usa_missions = np.char.find(locais, "USA")
usa_missions = usa_missions[usa_missions!=-1]
print(f"Missões realizadas pelos USA: {len(usa_missions)}")

# 4) Missão mais cara da SpaceX
companhia = valid_data[:,1]
spacex_missions = valid_data[companhia == "SpaceX"]
valores = spacex_missions[:,6]
spacex_missoes_caras = spacex_missions[valores == max(valores)]
print(f"Missões com custo = {max(valores)}\n{spacex_missoes_caras}")

# 5) Empresas x Qtd de missões
nomes_companhias, qtd_missoes = np.unique(companhia, return_counts=True)
for i in range(len(nomes_companhias)):
    print(f"{nomes_companhias[i]} - {qtd_missoes[i]} missões")
