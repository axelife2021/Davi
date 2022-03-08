último1 = 10
último2 = 20
fila1 = list(range(1,último1+1))
fila2 = list(range(1,último2+1))
while True :
    print ("\nExistem %d clientes na fila %d" % len(fila))
    print ("Fila atual:", fila)
    print ("Digite F para adicionar um cliente ao fim da fila,")
    print ("ou A para realizar o atendimento. S para sair.")
    operação = input ("Operação (F, A ou S):")
    if operação == "A":
        if (len(fila))>0:
            atendido = fila.pop(0)
            print ("Cliente %d atendido" % atendido)
        else:
            print ("Fila vazia! Ninguém para atender.")
    elif operação == "F":
        último+=1 # Incrementa o ticket do novo cliente
        fila.append(último)
    elif operação == "S":
        break
    else:
        print ("Operação inválida! Digite apenas F, A ou S!")