n = int(input("Digite um número inteiro: "))
divisor = 2
while divisor < n:
    if n % divisor != 0:
        print(divisor)
        divisor = 2*divisor - 1
if divisor >= n:
    if n == 1 or n == 0:
        print("%d não é primo." % n)
    else:
        print("%d é primo." % n) 

#Sem saída de dados!!!