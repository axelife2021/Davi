fim = int(input("Digite o último número a imprimir:"))
x = 1
while x <= fim:
    print(x)
    x = x + 1
if fim <= 0:
    print("Valor inválido! Digite um valor maior ou igual a 1!")