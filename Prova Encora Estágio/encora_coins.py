# -*- coding: utf-8 -*-
"""Encora_coins.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13yaQIdEinXd1KdjXij37_4n_ztkd1rt7
"""

def makeChange(n):
# essa função ira pedir ao usuário o número de centavos
    coins = [25, 10, 5, 1] 
    result = set()
    def helper(n, indice, current): 
#essa função encontra todas as combinações das moedas, sendo os parâmetro n = numero escolhido pelo usuário, indice = o indice da moeda no conjunto e current = armazena a combinação das moedas
        if indice == len(coins)-1:
            result.add(tuple(current + [n]))
            return
#aqui a gente verifica se o indice da moeda é igual ao ultimo indice da lista, caso seja verdade adicionammos ela na lista
        for i in range(n // coins[indice] + 1):
            current[indice] = i
            helper(n - i * coins[indice], indice + 1, current)
#o for verifica todas as possibilidades, começando em 0 e indo ate n centavos. Cada iteração atribui o valor da moeda ao indice da lista current, e a função helper é chamada novamente
    helper(n, 0, [0] * len(coins)) #aplicação das variaveis na função helper criada
    return result

makeChange(12)

makeChange(20)