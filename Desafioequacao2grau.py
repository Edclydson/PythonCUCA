# DESAFIO
'CRIAR UM PROGRAMA QUE RESOLVE UMA EQUAÇÃO DO 2º GRAU...'
from math import sqrt
a = int(input("Qual o valor de a?"))  # A variavel a necessita ser !=0
b = int(input("Qual o valor de b?"))
c = int(input("Qual o valor de c?"))

# utilizando bhaskara
# descobrindo o delta
delta = ((b**2) - (4 * a * c))
print("O delta é:", delta)

# substituindo na formula de bhaskara
x1 = (-b + sqrt(delta)) / (2 * a)
print("O valor de x1 é:", x1)

x2 = (-b - sqrt(delta)) / (2 * a)
print("O valor de x2 é:", x2)
