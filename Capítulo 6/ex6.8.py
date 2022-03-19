#Declaração da lista com valores escolhidos arbitrariamente
L= [15,7,27,39]
#Entrada do valor que deseja procurar
p = int(input("Digite o valor a procurar: "))
#Declarado índice inicial
x = 0
#Estrutura de repetição para comparar a variável com os elementos da lista
while x < len(L):
    #Se a variável p estiver na lista, a estrutura de repetição encerra
    if L[x] == p:
        break
    #Se não, compara com o próximo elemento da lista
    x = x+1
#Se não comparou com todos os elementos, quer dizer que p foi encontrado no índice x e essa mensagem é retornada ao usuário
if x <= len(L) -1:
    print("%d achado na posição %d" % (p,x))
#Se não, p não foi encontrado e isso é retornado ao usuário
else:
    print("%d não encontrado" % p)
