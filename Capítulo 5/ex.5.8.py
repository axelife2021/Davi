#Entrada dos fatores e de an para evitar erros de calculo
a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
an = 0
#Definicao do contador (iniciou com 0 para a multiplicacao apresentar o resultado esperado)
x = 0
#Condicao para limitar a soma em ate b vezes
while x < b:
    #Soma substituindo multiplicacao
    an = an + a
    #Operacao do contador
    x = x + 1
    #Saida do resultado
print(an)