#CLASSIFICANDO POR APROXIMACAO NUMERICA
def minhafuncao(n): #FUNCAO
    return abs(n - 50)  #ABS PARA VERIFICAR APROXIMACAO
    
numeros = [100,50,65,82,23]
numeros.sort(key = minhafuncao) #ORGANIZANDO DENTRO DA LISTA POR APROXIMACAO
print(numeros)