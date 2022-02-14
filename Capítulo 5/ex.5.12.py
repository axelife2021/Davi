#Entrada do valor da taxa de juros da poupança
taxa_de_juros = float(input("Digite a taxa de juros da poupança: "))
#Definir contador
n = 1
#Entrada do primeiro depósito
depósito = float(input("Digite o valor do depósito do mês %d: " %n))
montante = depósito
#Acumulação ao longo de 2 anos
while n <= 24:
    #Saída do valor do montante a cada final de mês
    print("Mês %d: R$ %7.2f" %(n,montante))
    novo_depósito = float(input("Digite o valor do depósito do mês %d: " %n))
    montante = montante + novo_depósito
    n = n + 1
    #Operação de juros compostos
    montante = montante + montante*(taxa_de_juros/100)
print("Montante total: R$ %7.2f" % montante)


#Ex.5.12 - como??????????
    