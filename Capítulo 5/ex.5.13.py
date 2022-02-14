dívida_inicial = float(input("Digite o valor da sua dívida inicial: "))
dívida_original = dívida_inicial
juro_mensal = float(input("Digite o valor da taxa de juros mensal: "))
valor_mensal_pago = (float(input("Digite o valor que pagará ao final de cada mês: ")))
n = 0
while dívida_inicial > 0:
    dívida_inicial = dívida_inicial*(1 + (juro_mensal/100))
    dívida_inicial = dívida_inicial - valor_mensal_pago
    n = n + 1
print("Você pagará sua dívida em %d mês(meses)." % n)
dívida_total = dívida_original*((1 + (juro_mensal/100))**n)
print("Sua dívida total é de R$ %7.2f." % dívida_total)
juros = dívida_total - dívida_original
print("Você pagará R$ %5.2f de juros." % juros)
