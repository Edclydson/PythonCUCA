'''Faça um programa que pesquisa nome de pessoa de uma lista com a letra "a" em seu nome, em seguida insira os nomes encontrados em uma nova lista'''

nomes = ["Joao","Elizete","Maria","Pedro","Ana","Jose"]
nomes2 = []
for i in nomes:
    if ("a" in i):
        nomes2.append(i)
print(nomes2)