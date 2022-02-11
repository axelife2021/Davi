#Entrada do dividendo e do divisor e de an para impedir erro no calculo
a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
#Definicao do contador (iniciou com 0 para a multiplicacao apresentar o resultado esperado)
x = 0
#Condicao para limitar a soma em ate b vezes
while a >= b:
    #Soma substituindo multiplicacao
    a = a - b
    x = x + 1
    #Saida do resultado
print("Quociente: %d" %x)
print("Resto: %d" %a)