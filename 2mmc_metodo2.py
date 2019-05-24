# -*- coding: utf-8 -*-

"""
autor: diego czel stepanha
data: 2019/05/20
program: encontra o mmc atraves do metodo de decomposição simultanea em 
    fatores primos
"""
from sympy import prime

lista_numeros = [2, 5, 6]
fatores_primos = []
mmc = 1

def dividir_fatores_primo(lista, primo):
    """ recebe uma lista e um primo, e faz a decomposicao simultanea
        e atribui o fator primo na lista fatores_primos caso primo seja um
        fator primo de algum numero
    """
    is_fator_primo = False
    for ind, num in enumerate(lista):
        if(num % primo == 0):
            is_fator_primo = True
            lista[ind] = int(num / primo)
    if(is_fator_primo == True):
        fatores_primos.append(primo)
    return is_fator_primo
    
contador_primo = 1
while(True):
    if(len(set(lista_numeros)) == 1 and 1 in set(lista_numeros)):
        """significa que somente resta o 1 na lista,
            então todos os numeros foram decompostos em fatores primos
        """
        print(lista_numeros)
        print(fatores_primos)
        for n in fatores_primos:
            mmc *= n
        print('mmc é ', mmc)
        break
    primo = prime(contador_primo)
    while(dividir_fatores_primo(lista_numeros, primo)):
        """usa o retorno bool da funcao para calcular a decomposicao dos 
            numeros enquanto for possivel dividir pelo numero primo
            quando não der irá para o proximo numero primo
        """
        continue
    contador_primo += 1
