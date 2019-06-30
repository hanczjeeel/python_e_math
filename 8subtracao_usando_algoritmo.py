
def sub(num1, num2):
    
    if('.' not in num1):    # se '.' não estiver em num1 ou num2
        num1 = num1 + '.0'  # adiciona no fim de num1 e num2 o valor '.0'
    if('.' not in num2):    # para facilitar a subtracao usando o algoritmo
        num2 = num2 + '.0'  #
    
    resultado = [] # armazena o resultado da soma entre num1 + num2

    if(float(num2) > float(num1)): # Faz a troca para que num1 seja maior que num2
        num1, num2 = num2, num1    # 
    
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

    for ind in range(len(num1)): # percore posicao a posicao da direita p/ esquerda
        if(num1[ind] == '.' and num2[ind] == '.'):    # ambas posições são '.'
            resultado.append('.')       # então append '.' no resultado
        else:
            if( int(num1[ind]) >= int(num2[ind]) ):            
                resultado.append(str( int(num1[ind]) - int(num2[ind]) ))                                    
            else:                                                            
                if( ind < len(num1) - 1 ): # cuidado com o indice da lista
                    if(num1[ind + 1] == '.'): # é o ponto então pegar proximo
                        num1[ind] = str( int(num1[ind]) + 10)
                        num1[ind + 2] = str( int(num1[ind + 2]) - 1 )
                        resultado.append(str( int(num1[ind]) - int(num2[ind]) ))
                    else: # significa que é menor então tem que emprestar
                        num1[ind] = str( int(num1[ind]) + 10)
                        num1[ind + 1] = str( int(num1[ind + 1]) - 1 )
                        resultado.append(str( int(num1[ind]) - int(num2[ind]) ))



    resultado.reverse()
    resultado = ''.join(resultado)
    return resultado
sub('555.550', '55.555')
sub('5', '4')
sub('5.25', '1.15')
sub('16.2', '4.25')
sub('2', '0.72')
