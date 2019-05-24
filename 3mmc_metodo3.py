# -*- coding: utf-8 -*-

"""
autor: diego czel stepanha
data: 2019/05/22
program: encontra o mmc atraves do metodo do produto das maiores potencias 
    dos fatores primos comuns e nao comuns
"""

from sympy import prime

lista_numeros = [12, 5, 6]
fatores_primos = {} # armazena num decomposto {12: {2: 2, 3: 1}} == 
#                                               12 = (2 ** 2) + ( 3 ** 1) == 2*2*3
potencias = {} # armazena as potencias das decomposicoes dos numeros

for num in lista_numeros:
    fatores_primos[num] = {}
    result = num # salva as divisoes sucessivas do num pelos primos
    posicao_primo = 1 # controla a geração dos primos
    while(True):
        if(result == 1): # se result for 1 significa que num foi decomposto
            break
        primo = prime(posicao_primo)
        if(result % primo == 0):
            result = int(result / primo)
            # controle de chave valor do dicio
            if(primo in fatores_primos[num].keys()):
                # se chave existir aumenta em 1 o valor
                fatores_primos[num][primo] = fatores_primos[num][primo] + 1
            else:
                fatores_primos[num][primo] = 1
        else: # modifica para o proximo primo
            posicao_primo += 1

print(fatores_primos)

# manipula dict potencias para armazenar cada primo e as potencias
# para então pegar o primo e sua maior potencia
for key1 in fatores_primos.keys():
    for key2 in fatores_primos[key1].keys():
        print(key2, fatores_primos[key1][key2])
        # controla as chaves e valores do dict potencias
        if(key2 in potencias.keys()):
            potencias[key2].append(fatores_primos[key1][key2])
        else:
            potencias[key2] = [fatores_primos[key1][key2]]
            
print(potencias)

mmc = 1
#processa o mmc percorendo o dict potencias com os primos e suas potencias
for chave in potencias.keys():
    print(chave, chave ** max(potencias[chave]))
    mmc = mmc * (chave ** max(potencias[chave]))
print('minimo multiplo comum', mmc)
