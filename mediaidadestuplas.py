#DESAFIO MEDIA DAS IDADES NAS TUPLAS
pessoas = [("ana",20,1.70),("ze",30,1.80),('pedro',25,1.60),('ana',18,1.60),('maria',22,1.63),('chico',30,1.70),('oscar',30,1.90),('joana',19,1.60),('val',21,1.70)]
media = 0
for p in range(len(pessoas)):
    idade = pessoas[p][1]
    media = media + idade
print("A media das idades é: ","%.1f" %(media/len(pessoas)))