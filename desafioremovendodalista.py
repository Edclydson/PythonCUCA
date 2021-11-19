#DESAFIO 
#lista com nome de 5 animais depois imprima a lista
#insira 2 animais no final da lista
#apague um animal da lista pele seu indice e imprima a lista

animais = ["Gato","Cachorro","Tartaruga","Papagaio","Galinha"]
print(animais)
animais.append("Vaca")
animais.append("Águia") #ADICIONANDO NOVOS ITENS AO FINAL DA LISTA
print(animais)
animais.remove("Cachorro") #REMOVENDO ITEM PELO CONTEÚDO
print(animais)
animais.pop(4) #REMOVENDO ITEM PELO INDICE DELE NA LISTA
print(animais)
