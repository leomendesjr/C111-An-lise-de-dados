# Exercícios Propostos 3 - Cap04
# Author: Daniel Jardim Nunes - GEC - 1525
# Teacher: Renzo - C111

import numpy as np

# Loading of the dataset space.csv
arr = np.loadtxt("space.csv",
                 delimiter=";",
                 dtype=str,
                 encoding="utf-8")

# Questão 01
cont = 0
cont1 = 0
arr1 = arr[:,7]
for c in arr1:
    if c == "Success":
        cont += 1
    cont1 += 1
Result = round((cont/cont1)*100,2)
print("Questão 01:\n","Success:",Result,"%\n")
"""
# Questão 02
cont = 0
cont1 = 0
arr1 = arr[1:,6]
for c in arr1:
    if float(c) > 0:
      cont += float(c)
    cont1 += 1
media = round((cont/cont1),2)
print("Questão 02:\n","Cost: R$",media,"\n")

# Questão 03
cont = 0
arr1 = arr[0:,2]
for c in arr1:
    if "USA" in c:
        cont += 1
print("Questão 03:\n","EUA:",cont,"missões\n")

# Questão 04
var = 0
arr1 = arr[1:,1]
arr2 = arr[1:,6]
arr3 = arr[1:,4]
for c in range(len(arr1)):
    if arr1[c] == "SpaceX":
        if float(arr2[c]) >= var:
            var = float(arr2[c])
            missao = arr3[c]
print("Questão 04:\n","Missão:",missao,"\n Custo: R$",var,"\n")
"""
# Questão 05
arr1 = arr[1:,5]
arr2 = arr[1:,1]
arr3 = arr[1:,0]
cont = 0
cont1 =0
print("Questão 05:\n")
for c in range(len(arr1)):
    cont1 += 1
    if arr1[c] == "StatusActive":
        print("Empresa:",arr2[c]," - Nº de Missões:",arr3[c],"\n")

