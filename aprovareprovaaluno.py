#DESAFIO 

#programa que pede a nota do aluno e diz se foi aprovado ou reprovado

nota1= float(input("digite a primeira nota: "))
nota2= float(input("digite a segunda nota: "))

media= (nota1 + nota2) / 2
if media>= 7:
    # aprovado
    print("Aluno Aprovado!")
else:
    print("Aluno Reprovado")