# -*- coding: utf-8 -*-
"""
autor: Diego Czel Stepanha
data: 2019/05/23
program:
    calcula o MDC atraves do metodo manul, encontrando os divisores e então 
    localizando o maior divisor comum.
"""

numeros = [180, 280, 300]
divisores = {}

# metodo que calcula os divisores de numero
def calcular_divisores(num):
    contador = 1
    div = []
    while(contador <= num):
        if(num % contador == 0):
            div.append(contador)
        contador += 1
    return div

# computador os divisores da lista numeros
for num in numeros:
    divisores[num] = calcular_divisores(num)

print(divisores)

# faz a intersecção dos conjuntos de divisores
div_comum = []
for num in divisores[numeros[0]]:
    is_divisor = True # controla se o divisor esta presente em todos conjuntos
    for chave in divisores.keys():
        if(num not in divisores[chave]):
            is_divisor = False
    if(is_divisor == True):
        div_comum.append(num)
        
print('o mdc é', max(div_comum))
