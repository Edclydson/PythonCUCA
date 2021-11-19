frutas= ["maça","banana","uva","maça","uva","laranja"]
lista1 = [x if x != "banana" else "abacate" for x in frutas]
print(lista1)