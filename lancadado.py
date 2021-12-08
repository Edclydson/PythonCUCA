'''
Faça um programa que simule um lançamento de dados. 
Lance o dado 100 vezes e armazene os resultados em um vetor. 
Depois, mostre quantas vezes cada valor foi conseguido. 
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, 
simulando os lançamentos dos dados.
'''

from random import *  # importando a biblioteca random


def dado():
    numeros = []
    for x in range(0, 101):
        # gerando os numeros aleatorios e inserindo
        numeros.append(randint(1, 6))
    print("O dado foi lançado 100 vezes!")
    for c in range(1, 7):
        print("O numero", c, "apareceu: ", numeros.count(c), "vezes")


dado()
