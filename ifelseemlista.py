frutas= ["maça","banana","uva","maça","uva","laranja"]
lista1 = [x if x != "banana" else "abacate" for x in frutas] #SE x FOR DIFERENTE DE banana ELE PASSA P/ O PROXIMO, SENÃO ELE INSERE abacate NO LUGAR
print(lista1)
