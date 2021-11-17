total=0
media=0
for x in range(0,5):
    input("Digite o nome da pessoa: ")
    idade=int(input("Digite a sua idade: "))
    total= total+idade
media = total/5
print("A soma de todas as idades é: ",total)
print("A média de todas as idades é: ",media)
