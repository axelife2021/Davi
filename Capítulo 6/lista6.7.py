números = [0,0,0,0,0]
x = 0
while x < 5:
    números[x] = int(input("Número %d: " % (x+1)))
    x += 1
while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    print("Vocẽ escolheu o número: %d" % (números[escolhido-1]))

#Caso o user digite um índice maior que o tamanho da lista, o programa dá erro.