#Entrada do número de primos que deseja que saia
n = int(input("Digite um número inteiro: "))
#Declarando candidato inicial para testar se é primo, contador e divisor inicial para o teste
candidato = 2
contador = 0
divisor = 2
#Repetições aninhadas(a primeira para atingir o número de primos solicitados; a segunda para checar se o candidato é primo)
while contador < n:
    while divisor < candidato:
        #Se a divisão for exata, o candidato não é primo
        if candidato % divisor == 0:
            break
        #Do contrário, testamos com os outros divisores menores do que o candidato
        else:
            divisor = 2*divisor - 1
    #Se todas as divisões testadas não deram exatas, o candidato é primo e será retornado ao usuário, contando 1 primo do total solicitado
    if divisor >= candidato:
        print(candidato)
        contador += 1
    #Reiniciando o divisor inicial para os testes com os próximos números
    divisor = 2
    #Declarando sucessor do candidato a ser testado
    candidato += 1