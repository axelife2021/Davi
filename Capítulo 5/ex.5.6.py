#Entrada de dados
n = int(input("Tabuada de: "))
#Contador
x = 1
#Condicao para exibir ate 2x10
while x <= 10:
    #Saida da expressao da tabuada
    print("%d x %d = " %(n, x), n*x)
    #operacao do contador
    x=x+1
