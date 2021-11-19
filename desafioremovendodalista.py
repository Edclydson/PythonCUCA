#DESAFIO 
#lista com nome de 5 animais depois imprima a lista
#insira 2 animais no final da lista
#apague um animal da lista pele seu indice e imprima a lista

animais = ["Gato","Cachorro","Tartaruga","Papagaio","Galinha"]
print(animais)
animais.append("Vaca")
animais.append("Águia")
print(animais)
animais.remove("Cachorro")
print(animais)
animais.pop(4)
print(animais)