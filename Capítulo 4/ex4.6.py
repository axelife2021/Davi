distância = float(input("Digite a distância a ser percorrida(km):"))
base = distância
if base < 200:
    preço = 0.5 * base
else:
    preço = 0.45 * base
print("Distância: %6.2f km ; preço da passagem: R$ %6.2f" % (distância, preço))