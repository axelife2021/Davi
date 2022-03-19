último1 = 10
fila1 = list(range(1,último1+1))
último2= 20
fila2 = list(range(1,último2+1))
fila = int(input("Digite o número da fila desejada (1 ou 2):"))
while fila != 1 and fila != 2:
    print("Valor inválido!")
    fila = int(input("Digite o número da fila desejada (1 ou 2):"))
if fila == 1:
    while True:
        print("\nExistem %d clientes na fila %d" % (len(fila1), fila))
        print("Fila atual:", fila1)
        print("Digite F para adicionar um cliente ao fim da fila,")
        print("ou A para realizar o atendimento. S para sair.")
        operação = input("Operação (F, A ou S):")
        if operação == "A":
            if (len(fila1)) > 0:
                atendido = fila1.pop(0)
                print("Cliente %d atendido" % atendido)
            else:
                print("Fila vazia! Ninguém para atendr.")
        elif operação == "F":
            último1 += 1
            fila1.append(último1)
        elif operação == "S":
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
elif fila == 2:
    while True:
        print("\nExistem %d clientes na fila %d" % (len(fila2), fila))
        print("Fila atual:", fila2)
        print("Digite F para adicionar um cliente ao fim da fila,")
        print("ou A para realizar o atendimento. S para sair.")
        operação = input("Operação (F, A ou S):")
        if operação == "A":
            if (len(fila2)) > 0:
                atendido = fila2.pop(0)
                print("Cliente %d atendido" % atendido)
            else:
                print("Fila vazia! Ninguém para atendr.")
        elif operação == "F":
            último1 += 1
            fila2.append(último2)
        elif operação == "S":
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
