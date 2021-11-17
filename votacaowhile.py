c1 = 0
c2 = 0
capurna = 4
voto = 0
totalvoto = 0
while(totalvoto<=capurna):
    voto = int(input("Em quem você vota? "))
    if(voto == 13):
        c1 = c1 + 1
    elif(voto == 15):
        c2 = c2 + 1
    totalvoto = totalvoto + 1

print("Total de pessoas que votaram: ", totalvoto)
print("Total de pessoas que votaram no candidato 1 : ", c1)
print("Total de pessoas que votaram no candidato 2 : ", c2)
    