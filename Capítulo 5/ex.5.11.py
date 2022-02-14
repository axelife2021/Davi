#Entrada dos valores do depósito inicial e da taxa de juros da poupança
depósito = float(input("Digite o valor do depósito inicial: "))
taxa_de_juros = float(input("Digite a taxa de juros da poupança: "))
#Definir contador e montante(acumulador)
n = 1
montante = depósito
#Acumulação ao longo de 2 anos
while n <= 24:
    #Operação de juros compostos
    montante = montante + montante*(taxa_de_juros/100)
    #Saída do valor do montante a cada final de mês
    print("Mês %d: R$ %7.2f" %(n,montante))
    
print("Montante total: R$ %7.2f" % montante)
