energia = float(input("Quantidade de kWh consumida:"))
tipo = int(input("Tipo de instalação (1-residencial, 2-industrial, 3-comercial):"))
base = energia
preço = 0
if tipo == 1:
    if base <= 500:
        preço = preço + (base*0.4)
        base = 500
    else:
        preço = preço + ((base - 500)*0.65)
if tipo == 2:
    if base <= 1000:
        preço = preço + (base*0.55)
        base = 1000
    else:
        preço = preço + ((base - 1000)*0.6)
if tipo == 3:
    if base <= 5000:
        preço = preço + (base*0.55)
        base = 5000
    else:
        preço = preço + (5000*0.55) + ((base - 5000)*0.6)        
print("Preço da conta de energia (%5.2f kWh): R$%5.2f" % (energia, preço))

#O computador não lê variável string? Selecionar tipo 1 com entrada da letra R de residencial, como?