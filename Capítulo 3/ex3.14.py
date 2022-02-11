#Input de dados
d = float(input("Digite a distância percorrida pelo usuário(km):"))
t = int(input("Digite o número de dias do aluguel:"))
#Dados armazenados
P = 60
p = 0.15
#Cálculo do pagamento
V = (P*t) + (p*d)
#Output
print("Valor a pagar: R$ %5.2f" % V)