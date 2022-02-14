#Entrada de compra para evitar problemas com nicho eletrônico
compra = 0
#Entrada dos preços do produtos
preço1 = 0.50
preço2 = 1.00
preço3 = 4.00
preço5 = 7.00
preço9 = 8.00
#Loop da entrada da compra
while True:
    #Entrada do código do produto
    código = int(input("Digite o código do produto ou 0 para encerrar: "))
    #Condição para encerrar o loop
    if código == 0:
        break
    #Entrada do produto de código 1 (esquema repetido para os códigos 2, 3, 5 e 9)
    if código == 1:
        #Entrada da quantidade do produto
        quantidade = int(input("Digite a quantidade a ser comprada: "))
        #Acumulador da compra
        compra = compra + preço1*quantidade
    elif código == 2:
        quantidade = int(input("Digite a quantidade a ser comprada: "))
        compra = compra + preço2*quantidade
    elif código == 3:
        quantidade = int(input("Digite a quantidade a ser comprada: "))
        compra = compra + preço3*quantidade
    elif código == 5:
        quantidade = int(input("Digite a quantidade a ser comprada: "))
        compra = compra + preço5*quantidade
    elif código == 9:
        quantidade = int(input("Digite a quantidade a ser comprada: "))
        compra = compra + preço9*quantidade
    #Restrição de entrada do código do produto
    else:
        print("Código inválido! 1, 2, 3, 5 e 9 são os códigos válidos!")
#Saída do total da compra
print("O valor total da compra é de R$ %5.2f" % compra)
    