#Declarando listas
A = [1,2]
B = [2,3]
#Comparando elementos das listas um a um usando del para retirar os elementos repetidos
if A[0] == B[0]:
    del A[0]
elif A[0] == B[1]:
    del A[0]
elif A[1] == B[0]:
    del A[1]
elif A[1] == B[1]:
    del A[1]
#Adicionando B em A
A.extend(B)
#Saída de A
print(A)

#Tentei usando contadores para indicar os índices dos elementos da lista (inicializando com zero), porém apareceram problemas sobre o index estar fora do range e sobre a operação de adicionar elementos não repetidos
#Esse código funciona para duas listas conhecidas e com dois elementos cada. Como seria para listas desconhecidas com vários elementos?
