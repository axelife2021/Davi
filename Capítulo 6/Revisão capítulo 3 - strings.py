#Revisão capítulo 3 - strings
print(len("A"))
print(len("AB"))
print(len(""))
print(len("No more bananas!"))
#len permite contar o número de caracteres dentro de uma string
a = "ABCDEF"
print(a[0])
print(a[1])
print(a[5])
#'string index out of range' - essa mensagem de erro indica que o índice especificado na função está fora dos limites da string
# Concatenação
cs = "ABC"
print(cs + "C")
print(cs + "D"*4)
print("<" + "_"*10 + ">")
print(cs + "x4 = " + cs*4)
#Composição 
idade = 19
print("%d" % idade)
print("%03d" % idade)
print("%3d" % idade)
print("[%-3d]" % idade)
nome = "Gabriel"
altura = 1.70
print("%s tem %d anos e %f m de altura." % (nome, idade, altura))
print("%12s tem %3d anos e %5.2f m de altura." % (nome, idade, altura))
print("%12s tem %03d anos e %5.2f m de altura." % (nome, idade, altura))
print("%-12s tem %-3d anos e %-5.2f m de altura." % (nome, idade, altura))
#Fatiamento
s = "ABCDEFGHI"
print(s[0:2])
print(s[1:2])
print(s[2:4])
print(s[0:5])
print(s[1:8])
#Fatiamento com índices negativos
print(s[:2])
print(s[1:])
print(s[0:-2])
print(s[:])
print(s[-1:])
print(s[-5:7])
print(s[-2:-1])