#Declaração de variáveis
dividendo = float(input("Digite o dividendo: "))
#Guardando o valor inicial do dividendo
n = dividendo
divisor = float(input("Digite o divisor: "))
#Condição para a operação de "divisão" continuar
while dividendo >= divisor:
    #Divisão usando subtração
    dividendo = dividendo - divisor
#Igualando o resto da divisão ao valor final do dividendo
resto = dividendo
#Saída do resto
print("O resto da divisão de %f por %f é %f" % (n, divisor, resto))