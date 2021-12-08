p = int(input("Quantas pessoas serão cadastradas?"))
totET = 0
preto = 0
for n in range(0, p):
    etnia = input("Qual a etnia? Preto, Branco ou Amarelo: ")
    if(etnia == "preto" or etnia == "preta"):
        totET = totET + 1
        preto = preto + 1
    elif(etnia == "branco" or etnia == "amarelo"):
        totET = totET + 1
perc = 100 * (preto/p)
print("Há", preto, "pessoas que se consideram Pretas! ")
print(perc, "%", "das pessoas cadastradas eram pretas!")
