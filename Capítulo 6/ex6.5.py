#Declarando limite da fila
último = 10
#Declarando fila de banco
fila = list(range(1,último+1))
#Saída de instruções sobre os comandos F, A e S
print ("\nExistem %d clientes na fila" % len(fila))
print ("Fila atual:", fila)
print ("Digite F para adicionar um cliente ao fim da fila,")
print ("ou A para realizar o atendimento. S para sair.")
#Entrada dos comandos como string
operação_string = input("Operação (F, A ou S):")
#Atribuindo chars da string a lista
operação = []
operação.extend(operação_string)
#Repetição das operações dos comandos até todos os chars esgotarem
while len(operação) > 0:
    #Extração do char
    char = operação.pop(0)
    #Operações para char igual a A (saída dos clientes atendidos)
    if char == "A":
        if (len(fila))>0:
            atendido = fila.pop(0)
            print ("Cliente %d atendido" % atendido)
        #Caso não haja mais clientes, saída de aviso de fila vazia
        else:
            print("Fila vazia! Ninguém para atender.")
    #Operações para char igual a F (entrada de clientes na fila)
    elif char == "F":
        último = último + 1
        fila.append(último)
    #Operação para encerrar repetição
    elif char == "S":
        break
    #Restrição de entrada de dados (é realmente necessário nesse caso?)
    else:
        print("Operação inválida! Digite apenas F, A ou S!")
   