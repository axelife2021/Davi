#Saída do menu
print("1 - adição")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")
#Entrada da opção desejada
menu = int(input("Digite o número da opção desejada: "))
#Estrutura da tabuada com repetições aninhadas (o modelo de repete para todas as operações, apenas se adequando a elas)
#Tabuada de adição
if menu == 1:
    tabuada = 1
    while tabuada <= 10:
        número = 1
        while número <= 10:
            print("%d + %d = %d" % (tabuada, número, tabuada+número))
            número += 1
        tabuada += 1
#Tabuada de subtração
if menu == 2:
    tabuada = 1
    while tabuada <= 10:
        número = 1
        while número <= 10:
            print("%d - %d = %d" % (tabuada, número, tabuada-número))
            número += 1
        tabuada += 1
#Tabuada de multiplicação
if menu == 3:
    tabuada = 1
    while tabuada <= 10:
        número = 1
        while número <= 10:
            print("%d x %d = %d" % (tabuada, número, tabuada*número))
            número += 1
        tabuada += 1
#Tabuada de divisão (mostrando o quociente inteiro, sem retornar o resto)
if menu == 4:
    tabuada = 1
    while tabuada <= 10:
        número = 1
        while número <= 10:
            print("%d / %d = %d" % (tabuada, número, tabuada//número))
            número += 1
        tabuada += 1