# calculando a área de um trapézio utilizando input no python
base_maior = int(input("Qual o tamanho da base maior? "))
base_menor = int(input("Qual o tamanho da base menor? "))
altura = int(input("Qual o tamanho a altura do trapezio? "))
area_trapezio = ((base_menor + base_maior) * altura) / 2
print("A área do trapézio é:", area_trapezio)
