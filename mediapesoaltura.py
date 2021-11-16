totalp = 0
totala = 0
media=0
for x in range(0,3):
    input("Digite o nome da pessoa: ")
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    totalp = totalp + peso
    totala = totala + altura
media = totalp/3
print("A media do peso das 3 pessoas é: ", media)
media = totala/3
print("A media de altura das 3 pessoas é: ", media)