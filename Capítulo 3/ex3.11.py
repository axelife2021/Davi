#Solicitar preço
v = float(input("Digite o valor da mercadoria:"))
#Solicitar desconto:
d = float(input("Digite o valor do desconto:"))
#Valor do desconto
D = (d/100)*v
#Preço a pagar
V = v - D 
#Output
print("Valor do desconto: %5.2f" % D)
print("Valor a pagar: %5.2f" % V)
