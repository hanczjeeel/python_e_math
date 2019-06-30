
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

    resultado = ''.join(resultado) # transforma em str o numero
    return resultado

def mul(num1, num2):
    # 1° contar casas decimais
    casas_decimais = 0
    if('.' in num1):
        num1 = num1.split('.')
        casas_decimais += len(num1[1])
        num1 = ''.join(num1) # 2° eliminar a virgula
    if('.' in num2):
        num2 = num2.split('.')
        casas_decimais += len(num2[1])
        num2 = ''.join(num2) # 2° eliminar a virgula
    
    # 3° multiplicar
    # 3.1° deixar maior numero na var num1
    if(len(num1) < len(num2)):
        num1, num2 = num2, num1
    # 3.2° inverter os numeros para trabalhar da direita para a esquerda
    num1 = num1[::-1] # inverte uma str
    num2 = num2[::-1] #
    resultado = [] # armazena o resultado
    sobrou = 0  # controla os acrescimos
                # 5 * 5 = 25
                # na matematica mantem o 5 e 
                # manda o 2 como acrescimo para somar na proxima multiplicação
    for ind,parte_baixo in enumerate(num2):
        mul_parte = []
        if(ind > 0):                    # controla a adição de zero a direita do numero exemplo:
            mul_parte.append('0' * ind) #  51 <-- parte de cima
                                        # *15 <-- parte de baixo
                                        #----
                                        # 255
                                        #+510  <---- este zero adicionado aqui
                                        #----
                                        # 765
        for parte_cima in num1:
            # não teve acrescimo
            if( ( int(parte_baixo) * int(parte_cima) + sobrou ) < 10 ): # 4 * 2 + 1 | parte_baixo * parte_cima + sobrou
                mul_parte.append(str( int(parte_baixo) * int(parte_cima) + sobrou ))
                sobrou = 0
            # teve acrescimo
            else:
                r = str( int(parte_baixo) * int(parte_cima) + sobrou )  # 5 * 3 + 2 | parte_baixo * parte_cima + sobrou = 17
                sobrou = int( r[0] ) # pega primeira posição            # 1 <-- sobrou 1 de acrescimo para proxima mult
                mul_parte.append( r[1] ) # ultima posição               # 7 <-- resultado
        if(sobrou > 0):                     # controla se houve acrescimo na ultima multiplicação
            mul_parte.append( str(sobrou) ) # se sobrou for maior que zero add o sobrou
            sobrou = 0                      # deixa em zero para proxima etapa
        mul_parte.reverse()             # inverte o numero pra ordem correta
                                        # ordem correta | ordem inversa (usada nos for que é o algoritmo de mul)
                                        # 25            |   52
                                        #*15            |  *51
                                        #---            |  ---
                                        #125            |   521
                                        #250+           |   052+ <-- zero vindo do controle de add do zero
                                        #---            |   ---
                                        #375            |   573

        mul_parte = ''.join(mul_parte)  # transforma em str a lista
        resultado.append(mul_parte)     # add no resultado cada multiplicação de cada parte

                                                                # Controla as somas das multiplicações
    soma = ''                                                   # armazena a soma total
    if(len(resultado) == 0):                                    #
        pass                                                    #
    elif(len(resultado) == 1):                                  # só teve uma multiplicação 
        soma = ''.join(resultado)                               # 
    elif(len(resultado) == 2):                                  # tem 2 multiplicações, chama function add e retira .0 
        soma = add(resultado[0], resultado[1]).replace('.0', '')# do fim
    else:                                                       #
        soma = add(resultado[0], resultado[1])                  # tem mais de 2 multiplicações, então faz for para
        for ind in range(2, len(resultado)):                    # somar todas e retira .0 do fim
            soma = add(soma, resultado[ind])                    #
        soma = soma.replace('.0', '')                           #
    
    if(casas_decimais == 0):                                        # Controla a adição da virgula
        return soma                                                 # soma[:-casas_decimais] inicio até antes da ,
    else:                                                           # soma[-casas_decimais:] depois da , até o fim
        return soma[:-casas_decimais] + '.' + soma[-casas_decimais:]#

print(mul('12.8', '0.07'))
print(mul('2.5', '1.5'))
print(mul('15.85', '16'))
print(mul('3.2', '2'))
print(mul('51', '15'))
