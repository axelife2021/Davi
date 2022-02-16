#Entrada do número
n = int(input("Digite um número inteiro: "))
#Declarando divisor inicial igual a 2
divisor = 2
#Estrutura de repetição para verificar se o número entrado é primo
while divisor < n:
    #Números primos são divisíveis por outros números que não sejam 1, -1, eles mesmos e seus opostos
    if n % divisor == 0:
        #Saída da mensagem
        print("%d não é primo." % n)
        #Encerrar repetição
        break
    #Os próximos divisores para a verificação devem ser ímpares
    else:
        divisor = 2*divisor - 1
#Caso o número passe na verificação
if divisor >= n:
    #1 e 0 não são primos (retornar essa mensagem)
    if n == 1 or n == 0:
        print("%d não é primo." % n)
    #Caso o número seja primo (retornar essa mensagem)
    else:
        print("%d é primo." % n) 