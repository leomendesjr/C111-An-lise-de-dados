import numpy as np

#Exercicio Proposto 1

#1
vetor = np.linspace(0,1,21)
print (vetor)

#2
vpar = np.arange(0,51,2)
print(vpar)
vpar1 = np.arange(50,101,2)
print(vpar1)
vconcate = np.concatenate((vpar,vpar1))
print(vconcate)
print(np.sort(vconcate))

#3
vord = np.flip(np.sort(vconcate))
print(vord)

#4
mtz = np.array([[1,1,1,1],[1,1,1,1],[1,1,1,1]])
print(mtz)
print(mtz.reshape(1,12))

#5
mtz1 = np.array([[1,2,3,4,5],[5,6,7,8,9],[9,10,11,12,12]])
x,y = np.shape(mtz1)
if((x*y)%2) == 0:
    print('Vetor com número par')
else:
    print('Vetor com número impar')   


#Exercicio Proposto 2
#1
np.random.seed(5)
vr = np.random.rand(10)
print(vr)
print(100*vr)
print(np.floor(100*vr))

#2
np.random.seed(10)
matriz = np.random.randint(50, size=(4, 4))
print(matriz)

#3
col = matriz.mean(axis=0)
lin = matriz.mean(axis=1)
print("Maior media das colunas é ",col.max())
print("Maior media das linhas é ",lin.max())

#4
numero, quantidade = np.unique(matriz, return_counts = True)
for i, j in enumerate(numero):
    print("Elemento",j," = ", quantidade[i])
print('------------------------------')
for i, j in enumerate(numero):    
    if(quantidade[i]) == 2:
        print("Elemento",j," = ", quantidade[i])



# Aula 3 cap 4

np.random.seed(10)
arr = np.random.randint(0,10,15)
print(arr)

#Fazendo um slicing em arr
arr2 = arr[0:4].copy()
#Alterando um elemento de arr2
arr2[0]=100
print(arr)
print(arr2)

#Trabalhando com o submodulo numpy.char

txt = "O Inatel e uma faculdade top demais"
print(np.char.find(txt, "faculdade"))

#verificar se possui apenas letra
#np.char.isaplha()
# verificar numero = np.char.isnum()

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
#print(spaceDS[6:,6])
quant_val = len(np.where(spaceDS[6:,6] > "120")[0])
soma = (np.where(spaceDS[6:,6] > "0")[0]).sum()
print(soma)
print(quant_val)