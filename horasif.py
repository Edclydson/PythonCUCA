#DESAFIO 

#programa que pede para o usuario digitar a hora e o programa informa bom dia, boa tarde, boa noite, boa madrugada

hora= int(input("que horas são? "))

if hora< 12 and hora>=6:
    #bomdia
    print("Bom dia!")
elif (hora<18 and hora>12):
    #boatarde
    print("Boa tarde!")
elif (hora>18 and hora<=23):
    #boanoite
    print("Boa noite!")
else:
    #boamadrugada
    print("Boa madrugada!")