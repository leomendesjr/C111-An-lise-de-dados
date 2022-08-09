# Nomes é o nome do elemento criado para exemplo 
# se der um print(type(nomes)), indica o tipo do elemento

#Coleções em python
# 1-Tupla
# Guardam os dados dentro de ()
# Estrutura imutavel

#Slicing

# nomes[i:j] -> i - inclusive e j - exclusive

###########################
# Lista

# Armazena seus dados dentro de []
# Coleção mutavel

# Insercao de elementos
# APPEND - insere no final
# nomes.append('BULMA')
# INSERT - insere baseando no indice
# nomes.insert(1,'Kuririn')

# Exclusao de elementos
# POP - exclui por indice
# nomes.pop(2)
# REMOVE - exclui por valor
# nomes.remove('Goku')

# Conjuntos
# Nao guardar os indices de seus elementos
# Armazena seus dados dentro de {}
# Nao guarda elementos repetidos

# AD - adicionar dados
# UPDATE - atualizar elementos
# REMOVE - excluir elementos
# nomes.remove(x)

# Dicionários
# Guarda seus elementos dentro de {}
# Usa indices customizaveis no padrao - chave:valor


"""
#Ex 1

tabela = ["Real", "Borussia", "Bayern","Barcelona", "Psg"]

#3 primeiros
print(tabela[:3])
#2 ultimos
print(tabela[3:])
#Ordem Alfabetica
print(sorted(tabela))
#Posicao do Barcelona
print(tabela.index("Barcelona"))

#Ex 2
l1 = {'Iphone 13','Xiaomi 8','Samsung 22', 'Xiaomi 9','Iphone 13'}
l2 = {'Samsung 22', 'Xiaomi 9','Iphone 13','Iphone 11','Iphone 8'}

print("Todos modelos disponiveis: ")
print(l1 | l2)
print("Modelos em ambas as lojas: ")
print(l1 & l2)

"""
#Ex 3

info = {}
nome = input('Entre com o nome do aluno: ')
media = float(input('Entre com a media do aluno: '))
info['Nome: '] = nome
info['Media: '] = media

if media >= 60:
    sf = 'AP'
else:
    sf = 'RP'
info['Situacao: '] = sf
print(info.items())