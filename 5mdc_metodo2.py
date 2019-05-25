# -*- coding: utf-8 -*-

"""
autor: Diego Czel Stepanha
data: 2019/05/24
program:
    calcula o mdc através do metodo 2 divisoes sucessivas de euclides,
    este metodo calcula o mdc somente de 2 numeros simultaneos.
    logo para calcular o mdc de varios numeros, precisa ir calculando o mdc
    par a par.
    exemplo:
        num1, num2, num3
        mdc(num1, num2) dai mdc(result, num3)
"""
numeros = [280, 300, 180]
numeros.sort(reverse = True)
def mdc_euclides(maior, menor):
    dividendo = maior
    divisor = menor
    resto = dividendo % divisor
    while(True):
        if(resto == 0):
            return divisor
        dividendo = divisor
        divisor = resto
        resto = dividendo % resto

while(len(numeros) != 1): # se len == 1 significa que só restou o mdc na list numeros
    mdc = mdc_euclides(numeros[0], numeros[1])
    del numeros[0]
    del numeros[0]
    numeros.append(mdc)

print('mdc é',numeros)
