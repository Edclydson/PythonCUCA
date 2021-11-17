c1 = 0
c2 = 0
c3 = 0
c4 = 0
branco = 0
capurna = 10
voto = 0
totalvoto = 0
while(totalvoto<=capurna):
    voto = int(input("Em quem você vota? "))
    if(voto == 13):
        c1 = c1 + 1
    elif(voto == 15):
        c2 = c2 + 1
    elif(voto == 20):
        c3 = c3 + 1
    elif(voto == 30):
        c4 = c4 + 1
    else:
        branco = branco + 1
    totalvoto = totalvoto + 1

print("Total de pessoas que votaram: ", totalvoto)
print("Total de pessoas que votaram no candidato 1 : ", c1)
print("Total de pessoas que votaram no candidato 2 : ", c2)
print("Total de pessoas que votaram no candidato 3 : ", c3)
print("Total de pessoas que votaram no candidato 4 : ", c4)
print("Total de pessoas que votaram branco : ", branco)
    