def add(num1, num2):

    if('.' not in num1):    # se '.' não estiver em num1 ou num2
        num1 = num1 + '.0'  # adiciona no fim de num1 e num2 o valor '.0'
    if('.' not in num2):    # para facilitar a soma usando o algoritmo
        num2 = num2 + '.0'  #

    resultado = [] # armazena o resultado da soma entre num1 + num2

    num1, num2 = num1.split('.'), num2.split('.') # separa em list [inteira, decimal] num1 e num2

    if(len(num1[1]) > len(num2[1])): # parte decimal de num1 é maior que parte decimal de num2
        num2[1] = num2[1] + ( '0' * ( len(num1[1]) - len(num2[1]) ) ) # então adiciona 0 ao fim de num2
    else: # parte decimal de num2 é maior que parte decimal de num1
        num1[1] = num1[1] + ( '0' * ( len(num2[1]) - len(num1[1]) ) ) # então adiciona 0 ao fim de num1

    if(len(num1[0]) > len(num2[0])): # parte inteira de num1 é maior que parte inteira de num2
        num2[0] = ( '0' * ( len(num1[0]) - len(num2[0]) ) ) + num2[0] # então adiciona 0 no inicio de num2
    else: # parte inteira de num2 é maior que parte inteira de num1
        num1[0] = ( '0' * ( len(num2[0]) - len(num1[0]) ) ) + num1[0] # então adiciona 0 no inicio de num1

    num1, num2 = '.'.join(num1), '.'.join(num2) # gera str 'parte inteira' + '.' + 'parte decimal'

    num1, num2 = list(num1), list(num2) # separa em list colocando virgula em baixo de virgula

    num1.reverse() # inverte a list por causa que algoritmo da soma faz suas operações
    num2.reverse() # da direita para esquerda

    sobrou = 0 # controla se houve acrescimo em uma operação, digamos 8 + 5 resulta em 3 e sobra 1

    for n1, n2 in zip(num1, num2): # percore posicao a posicao da direita p/ esquerda
        if(n1 == '.' and n2 == '.'):    # ambas posições são '.'
            resultado.append('.')       # então append '.' no resultado
        else:
            if( ( int(n1) + int(n2) + sobrou ) < 10):            #operações que não tem sobra
                resultado.append(str(int(n1) + int(n2) + sobrou))#8 + 1 + 0 | num1 + num2 + sobrou
                sobrou = 0                                       #5 + 2 + 1 | num1 + num2 + sobrou
            else:                                                            #operações que tem sobra
                resultado.append( str(( int(n1) + int(n2) + sobrou ) - 10 )) #8 + 2 + 0 | num1 + num2 + sobrou
                sobrou = 1                                                   #5 + 7 + 1 | num1 + num2 + sobrou

    if(sobrou == 1):          # controla a ultima operação
        resultado.append('1') # se for 1 significa que teve operação 8 + 5 e o reseultado deve ser 13 e nao 3

    resultado.reverse()     # inverte para ficar na ordem correta
    print('.' in resultado)
    resultado = ''.join(resultado) # transforma em str o numero
    return resultado

print(add('912', '88'))
print(add('321.56', '38.6742'))
print(add('0.005', '0.005'))
print(add('0.1','0.2'))
print(add('15.0','10.0'))
