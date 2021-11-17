pessoas = []
for x in range(5):
    nome = input("digite um nome: ")
    pessoas.append(nome)
print(pessoas)
n = input("digite o nome a ser procurado na lista: ")
for x in range(0,5):
    if(pessoas[x]==n):
        print("Nome existente na lista!!!")
    else:
        print("Nome não consta na lista!!!")
        break
    