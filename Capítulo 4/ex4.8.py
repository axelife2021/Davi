a = 4
b = 6
operação = int(input("Digite a operação desejada (soma-1, subtração-2, multiplicação-3, divisão-4):"))
if operação == 1:
    resultado = a + b
elif operação == 2:
    resultado = a - b
elif operação == 3:
    resultado = a * b
elif operação == 4:
    resultado = a / b
else:
    print("Operação inválida, digite 1(soma), 2(subtração), 3(multiplicação) ou 4(divisão)!")
    quit()
print("Operação solicitada: %d ; resultado: %5.2f" % (operação, resultado))

#função quit() usada para encerrar o script.