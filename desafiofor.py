# DESAFIO
# PROGRAMA QUE PEDE NOME, SEXO, IDADE, COR DOS OLHOS(PRETO, CASTANHO OU VERDE), COR DO CABELO(PRETO, LOIRO, BRANCO)
# O PROGRAMA DEVERÁ CALCULAR E MOSTRAR O TOTAL DE HOMENS E O TOTAL DE MULHERES
# O PROGRAMA TAMBEM DEVERÁ MOSTRAR O TOTAL DE PESSOAS MENORES DE IDADE
# O TOTAL DE PESSOAS DE OLHOS PRETOS
# O TOTAL DE PESSOAS DOS CABELOS BRANCOS
p = int(input("Quantas pessoas serão cadastradas?"))
totH = 0
totM = 0
totMI = 0
totOP = 0
totCB = 0
for n in range(0, p):
    nome = input("Qual o nome? ")
    sexo = input("Qual o sexo? ")
    # SEXO
    if sexo == "masculino":
        totH = totH + 1
    elif sexo == "feminino":
        totM = totM + 1
    idade = int(input("Qual a idade? "))
    # MENOR DE IDADE
    if idade < 18:
        totMI = totMI + 1
    olhos = input("Qual a cor dos olhos? Castanhos, Preto ou verde: ")
    # COR DOS OLHOS
    if olhos == "pretos":
        totOP = totOP + 1
    cabelos = input("Qual a cor dos cabelos? Preto, Loiro ou Branco: ")
    # COR DOS CABELOS
    if cabelos == "branco":
        totCB = totCB + 1

print("Total de Homens: ", totH)
print("Total de Mulheres: ", totM)
print("Total de Menores de idade: ", totMI)
print("Total de Pessoas com olhos pretos: ", totOP)
print("Total de Pessoas com cabelos brancos: ", totCB)
