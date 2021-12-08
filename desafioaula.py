#EXERCICIOS TIRADOS DO SITE: https://wiki.python.org.br/ListaDeExercicios
#ESCOLHER ENTRE OS ITENS 1,2,3 E 4 // CADA ITEM POSSUI DIVERSAS QUESTÕES 
#QUESTÃO 17 DO ITEM 1

''' Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros; V
- comprar apenas galões de 3,6 litros; V
- misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. V
'''
#VARIAVEIS
mquad = float(input("Quantos metros tem a área a ser pintada? m²: "))
litrosn = float(mquad / 6)  #FORMULA PARA SABER QUANTOS LITROS DE TINTA SERAO NECESSARIOS
porclitros =float(litrosn + (litrosn*0.10))   #ADICIONANDO OS 10%
#ARREDONDANDO VALORES PARA +
quantgaloes = round((porclitros/3.6))  
quantlatas = round((porclitros/18))

#GALAO DE 3,6
if(porclitros<18):
    #CALCULANDO SE HAVERA SOBRAS OU SE FALTARA
    res =  (quantgaloes * 3.6) - porclitros
    if(res!=0 and res > 0):
        print("%.1f" %res,"litros restantes!")
    elif(res<0):
        print("%.1f" %res,"litros faltantes!")
    else:
        print("Não haverá sobras!")

    #SE A QUANTIDADE DE LITROS NECESSARIOS FOR MENOR QUE 3,6L
    if(quantgaloes<1):
        print("Será necessário menos de 1 galão de tinta de 3,6L")
    elif(quantgaloes==5): #SE A QUANTIDADE DE GALOES RESULTAR EM 18L 
        print("Será necessário ","%.1f" %litrosn," litros de tinta para pintar a área informada! Adicionando os 10%, a quantidade total de litros necessário é:","%.1f" %porclitros,"litros")
        print("Recomendamos comprar",quantlatas,"latas de 18L ,que custa R$80,00")    
    else:
        print("Será necessário ","%.1f" %litrosn," litros de tinta para pintar a área informada! Adicionando os 10%, a quantidade total de litros necessário é:","%.1f" %porclitros,"litros")
        print("Recomendamos comprar",quantgaloes,"galões de 3,6L ,que custa R$25,00")
        #CALCULANDO O VALOR DA COMPRA
        valorcompra = quantgaloes * 25
        print("O total da compra será de: R$","%.2f" %valorcompra)
        
#GALAO DE 18
elif(porclitros>=18):
    #CALCULANDO SE HAVERA SOBRAS OU SE FALTARA
    res2 = (quantlatas * 18) - porclitros
    if(res2!=0 and res2 > 0):
        print("%.1f" %res2,"litros restantes!")
    elif(res2<0):
        print("%.1f" %res2,"litros faltantes!")
    else:
        print("Não haverá sobras!")

    print("Será necessário ","%.1f" %litrosn," litros de tinta para pintar a área informada! Adicionando os 10%, a quantidade total de litros necessário é:","%.1f" %porclitros,"litros")
    print("Recomendamos comprar",quantlatas,"latas de 18L ,que custa R$80,00")
    #CALCULANDO O VALOR DA COMPRA
    valorcompra = quantlatas * 80
    print("O total da compra será de: R$","%.2f" %valorcompra)
        