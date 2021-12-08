# gerando numeros randomicos

from random import *  # importando a biblioteca random
numeros = []
total7 = 0
for x in range(0, 50):
    numeros.append(randint(1, 10))  # gerando os numeros aleatorios e inserindo
    if(numeros[-1] == 7):  # verificando quantos numeros 7 aparecem
        total7 = total7 + 1
print(numeros)
print(total7)
