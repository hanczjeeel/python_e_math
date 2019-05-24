# -*- coding: utf-8 -*-
# autor Diego Czel Stepanha
# data 2019-05-12
# encontrar o MMC no metodo 1 (manual), gerando os multiplos de cada numero
# e gerando os multiplos maximos de cada numero.
# 2, 5, 6 gera os maximos 4, 10, 12
# vai executar até encontrar os maximos como 30, 30, 30 ou seja é o mmc

numeros = [2, 5, 6]
numeros.sort(reverse=True) # deixar do maior para o menor

# criar chaves e valores [0] no dict multiplos
multiplos = {}
for num in numeros:
    multiplos[num] = [0]
    
chave = numeros[0] # maior numero que controla a geração dos multiplos
del numeros[0] # exluir o maior numero

while(True):
    maximos = [] # usado para inserir os maximos 
    # gera o multiplo do numero chave
    multiplos[chave].append(max(multiplos[chave]) + chave)
    maior = max(multiplos[chave])
    maximos.append(maior)
    #percorre os numeros gerando os multiplos até o maximo
    for num in numeros:
        while(True):
            multiplos[num].append(max(multiplos[num]) + num)
            aux = max(multiplos[num])
            if(aux >= maior):
                maximos.append(aux)
                break
    #se o set dos maximos for len 1 significa que é o multiplo
    if(len(set(maximos)) == 1):
        print('minimo multiplo comum', set(maximos))
        break
    

print(multiplos)
print(numeros)
