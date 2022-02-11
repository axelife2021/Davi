imóvel = float(input("Valor do imóvel:"))
salário = float(input("Valor do salário:"))
anos = int(input("Quantidade de anos a pagar o imóvel:"))
prestação = imóvel/(anos * 12)
if prestação > 0.3 * salário:
    print("O empréstimo foi reprovado! O valor da prestação mensal é de R$%5.2f" % prestação)
else:
    print("O empréstimo foi aprovado! O valor da prestação mensal é de R$%5.2f" % prestação)
