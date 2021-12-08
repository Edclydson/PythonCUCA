p = int(input("Quantas pessoas serão cadastradas?"))
totH = 0
totM = 0
for n in range(0,p):
    nome=input("Qual o nome? ")
    sexo=input("Qual o sexo? ")
    if sexo =="masculino":
        totH= totH + 1
    elif sexo == "feminino":
        totM = totM + 1
print("Total de Homens: ", totH)
print("Total de Mulheres: ", totM)