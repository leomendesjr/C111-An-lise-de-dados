# Exercicio 1
nome = input('Qual o seu nome')
print(nome.upper())
print(nome.lower())
print(nome.__len__())
print(nome.replace(nome,'do Inatel'))

#Exercicio 2
num = int(input('Qual o numero da tabuada: '))
opcao = int(input('Qual a quant de repetição: '))
opcao2 = int(input('Qual a quant: '))

for c in range(opcao,(opcao2+1)):
    print(c,'x',num,'=',num*opcao2)

#Exercicio 3

sex = input('Digite o sexo: ')
while sex != 'M' and sex != 'F':
    sex = input('Digite o sexo: ')

if sex == 'M':
    print('Masculino')
elif sex == 'F':
    print('Feminino')            