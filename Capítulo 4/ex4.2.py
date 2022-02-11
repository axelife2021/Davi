#Input de dados
v = float(input("Qual a velocidade do seu carro em km/h? "))
if v > 80:
    print("Você foi multado!")
    M = (v - 80) * 5
    print("Valor da multa: R$ %5.2f" % M)
if v <= 80:
    print("Você escapou dessa!")