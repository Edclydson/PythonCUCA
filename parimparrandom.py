# numeros randomicos

from random import * #importando a biblioteca random
numeros = []
totalp = 0
totali = 0
for x in range(0,10):
    numeros.append(randint(1,10)) #gerando os numeros aleatorios e inserindo 
    if(numeros[-1]%2 == 0):   #verificando se os numeros sao pares
        totalp = totalp + 1
    else:
        totali = totali + 1
print (numeros)
print ("Pares: ",totalp)
print ("Impar: ",totali)