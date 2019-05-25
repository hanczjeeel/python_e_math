# -*- coding: utf-8 -*-
"""
autor: Diego Czel Stepanha
data: 2019/05/25
program:
    Calcula o mdc através da decomposição em fatores primos de cada numero, 
    depois utiliza do produto dos fatores primos COMUNS de MENOR EXPOENTE
"""
from sympy import prime

numeros = [660, 780, 900]

fatores_primos = {} # armazena num decomposto {12: [2, 2, 3]} == 2*2*3
potencias = {}
# function que recebe num e faz a decomposicao em fatores primos
def decompor_fatores_primos(num):
    result = num
    fatores = {}
    posicao_primo = 1
    while(True):
        if(result == 1): # significa que num foi decomposto
            return fatores
        primo = prime(posicao_primo)
        if( result % primo == 0):
            result = int( result / primo )
            if(primo in fatores.keys()):
                fatores[primo] = fatores[primo] + 1
            else:
                fatores[primo] = 1
        else: # controla a geração do proximo primo
            posicao_primo += 1

# calcula as decomposições dos numeros
for num in numeros:
    fatores_primos[num] = decompor_fatores_primos(num)

# manipula o dict fatores_primos para guardar o primo e as potencias que tem nos 
# numeros
# a logica aqui é pegar o primo cujo list tiver o tamanho igual a list numeros
# exemplo: 2: [1, 2, 3] e list numeros [2, 4, 8], significa que o 2
# é um divisor comum dos 3 numeros.
for key1 in fatores_primos.keys():
    for key2 in fatores_primos[key1].keys():
        # controla as chaves e valores do dict potencias
        if(key2 in potencias.keys()):
            potencias[key2].append(fatores_primos[key1][key2])
        else:
            potencias[key2] = [fatores_primos[key1][key2]]

print(fatores_primos)     
print(potencias)

# calcula o mdc
mdc = 1
for chave in potencias.keys():
    # significa que o primo divide todos os numeros
    if(len(potencias[chave]) == len(numeros)):
        # faz o produto dos primos comuns e suas menores potencias
        mdc = mdc * (chave ** min(potencias[chave]))
    
print('o mdc é ', mdc)
