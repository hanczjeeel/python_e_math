import re

def div(num1, num2):
    # 1° igualar as virgulas se for decimal
    if('.' in num1 or '.' in num2):
        if('.' not in num1):
            num1 += '.0'
        if('.' not in num2):
            num2 += '.0'
        # 2° add zero nas casas decimais
        num1, num2 = num1.split('.'), num2.split('.') # separa em list [inteira, decimal] num1 e num2
        if(len(num1[1]) > len(num2[1])): # parte decimal de num1 é maior que parte decimal de num2
            num2[1] = num2[1] + ( '0' * ( len(num1[1]) - len(num2[1]) ) ) # então adiciona 0 ao fim de num2
        else: # parte decimal de num2 é maior que parte decimal de num1
            num1[1] = num1[1] + ( '0' * ( len(num2[1]) - len(num1[1]) ) ) # então adiciona 0 ao fim de num1
        # 3° ignorar a virgula
        num1, num2 = ''.join(num1), ''.join(num2)
        # 4° ignorar zeros a esquerda se e somente se 0 for o 1° digito
                                        # retira zeros a esquerda ddo num1 e num2
        num1 = re.sub("^0+", '', num1)  # ^ começo da str
                                        # 0 caracter no começo
        num2 = re.sub("^0+", '', num2)  # + significa incluir todos 0 do inicio da str
    #------------------------------Algoritmo da divisao---------------------------------#
    casas_decimais = 0 # controla quantas casas decimais tem                            #
    quociente = ''                                                                      #
    dividendo = int(num1)                                                               #
    divisor = int(num2)                                                                 #
    #---------------------controla a adicao dos zeros e do .-----------------------#    #
    if(dividendo < divisor): # add .0 se dividendo < divisor                       #    #
        casas_decimais += 1                                                        #    #
        quociente += '0.'                                                          #    #
        dividendo *= 10 # como adiciona um zero ao dividendo multiplica por 10     #    #
    while(dividendo < divisor):                                                    #    #
        casas_decimais += 1                                                        #    #
        quociente += '0'                                                           #    #
        dividendo *= 10 # como adiciona um zero ao dividendo multiplica por 10     #    #
    #------------------------------------------------------------------------------#    #
    while(True):                                                                        #
        if(dividendo < divisor):                                                        #
            casas_decimais += 1                                                         #
            if('.' not in quociente):                                                   #
                quociente += '.'                                                        #
                dividendo *= 10                                                         #
            else:                                                                       #
                #quociente += '0'                                                       #
                dividendo *= 10 # como adiciona um zero ao dividendo multiplica por 10  #
        else:                                                                           #
            quociente += str(dividendo // divisor)                                      #
            dividendo = dividendo % divisor                                             #
        if(dividendo == 0 or casas_decimais > 10):                                      #
            break                                                                       #
    #-----------------------------------------------------------------------------------#
    return quociente

print(div('0.4', '2'))
print(div('0.4', '0.2'))
print(div('0.125', '2.5'))
print(div('8', '0.25'))
print(div('3', '2'))
print(div('21', '9'))
print(div('3', '4'))
print(div('22','7'))
