print("Você fuma? Saiba quanto tempo você perdeu!")
#Input de dados
c = int(input("Quantos cigarros você fuma por dia? "))
a = float(input("A quantos anos você fuma ou já fumou? "))
#Dados armazanados
t1 = 10
#Cálculo da redução
t = (t1*c*365*a)
#Coversão
T = t/(24*60)
#Output
print("Seu tempo de vida reduziu %d dias!" % T)