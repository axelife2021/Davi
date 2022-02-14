s = 0
c = 0
while True:
    n = int(input("Digite um número para somar ou 0 para sair:"))
    if n == 0:
        break
    s = s + n
    c = c + 1
print("Você digitou %d números." % c)
print("A soma total vale %d." % s)
média = s/c
print("A média simples dos números digitados é %3.3f." % média)