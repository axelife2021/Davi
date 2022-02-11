salário = float(input("Salário do funcionário: "))
base = salário
if base > 1250:
    aumento = base * 0.10
if base <= 1250:
    aumento = base * 0.15
print("Salário: R$ %6.2f ; aumento: R$ %6.2f" % (salário, aumento))