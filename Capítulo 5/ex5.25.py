número = float(input("Digite um número positivo: "))
while número < 0:
    print("Valor inválido!")
    número = float(input("Digite um número positivo: "))
b = 2
p = (b+(número/b))/2
while número - (p*p) < 0.001:
    b = p
    p = (b+(número/b))/2
print("Raiz de %f: %f" % (número,p))

