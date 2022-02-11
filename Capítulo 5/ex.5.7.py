#Entrada de dados
n = int(input("Tabuada de: "))
a1 = int(input("Digite por onde quer começar a tabuada: "))
an = int(input("Digite onde quer terminar a tabuada: "))
#Contador
x = a1
#Condicao para exibir ate 2x10
while x <= an:
    #Saida da expressao da tabuada
    print("%d x %d = " %(n, x), n*x)
    #operacao do contador
    x=x+1
