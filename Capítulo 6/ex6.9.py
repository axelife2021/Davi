#Declarando lista dada pelo exercício
L = [15,7,27,39]
#Entrada de variáveis que desejam ser encontradas
p = int(input("Digite o primeiro valor a procurar: "))
v = int(input("Digite o segundo valor a procurar: "))
#As variáveis achou servem para decidir, no final, a mensagem a retornar ao usuário
achou_p = False
achou_v = False
#Declarando índice iniciais dos elementos a começarem a ser comparados com as variáveis
a = 0
b = 0
#Estrutura de repetição que compara a variável p com os elementos da lista
while a < len(L):
    #Se p foi achado, a estrutura cessa e achou_p passa a ser True
    if L[a] == p:
        achou_p = True
        break
    #Se não, o próximo elemento é comparado a p
    a += 1
#Estrutura de repetição que compara a variável v com os elementos da lista(mesma mecânica da estrutura anterior)
while b < len(L):
    if L[b] == v:
        achou_v = True
        break
    b += 1
#Se p foi achado primeiro, retorna-se isso mais a posição em que foi achado
if a < b:
    if achou_p:
        print("%d achado primeiro na posição %d" % (p,a))
    #Se não foi achado, retorna que não foi encontrado
    else:
        print("%d não encontrado" % p)
    #Se achou v, retorna isso e a posição que foi encontrado
    if achou_v:
        print("%d achado na posição %d" % (v,b))
    #Se não, retorna isso
    else:
        print("%d não encontrado" % v)
#Se v foi achado primeiro, retorna-se isso mais a posição em foi encontrado
elif a > b:
    if achou_v:
        print("%d achado primeiro na posição %d" % (v,b))
    #Se não foi encontrado primeiro, retorna isso
    else:
        print("%d não encontrado" % v)
    #Se achou p, retorna isso e a posição em que foi encontrado
    if achou_p:
        print("%d achado na posição %d" % (p,a))
    else:
        print("%d não encontrado" % p)
#Se p e v não foram encontrados, retorna isso
elif achou_p == False and achou_v == False:
    print("%d e %d não encontrados" % (p,v))

# Tem como reduzir/simplificar esse código?