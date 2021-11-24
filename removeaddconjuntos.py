#ADICIONANDO LISTAS E TUPLAS EM CONJUNTOS
clubes={"vasco","santos","gremio","cruzeiro"}
times=["flamengo","atletico"]
futebol=("internacional",)
clubes.update(times)
clubes.update(futebol)
print(clubes)

#REMOVENDO ITENS DOS CONJUNTOS
clubes.remove("cruzeiro")
clubes.discard("gremio")
print(clubes)