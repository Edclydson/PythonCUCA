#DESAFIO
#PROGRAMA QUE CADASTRA 3 NOTAS DE UM ALUNO EM UMA LISTA
#CALCULA E MOSTRA A MEDIA AO FINAL

notas = []
media = 0
n1= 0
n2 =0
n3 = 0

n1 = float(input("Informe a 1º nota: "))
notas.append(n1)
n2 = float(input("Informe a 2º nota: "))
notas.append(n2)
n3 = float(input("Informe a 3º nota: "))
notas.append(n3)
mediafinal = (notas[0]+notas[1]+notas[2]) / 3
print("A media final é:"," %.1f" %mediafinal)