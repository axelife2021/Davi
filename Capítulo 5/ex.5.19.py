valor = float(input("Digite o valor a pagar: "))
cédulas = 0
atual = 50
apagar = valor
moedas = 0
while True:
    if atual <= apagar:
        apagar -= atual
        cédulas += 1
    else:
        print("%d cédula(s) de R$ %d" % (cédulas, atual))
        if apagar < 1:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cédulas = 0
atual = 0.50
while True: 
    if atual <= apagar:
        apagar -= atual
        moedas += 1
    else:
        print("%d moeda(s) de R$ %5.2f" % (moedas, atual))
        if apagar == 0:
            break
        if atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        moedas = 0

#Problema na saída: como resolver?
        


