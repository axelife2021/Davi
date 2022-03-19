#Script para checar se um número é palíndromo
#Um número é palindromo se seu primeiro algarismo for igual ao último, se seu segundo for igual ao penúltimo e assim por diante, ou seja, se representar o mesmo número de trás para frente

#Entrada do número a analisar como string
número = input("Digite um número: ")
#Declarando lista que vai receber cada algarismo do número como elemento
teste = []
teste.extend(número)
#Declarando contador, índice inicial da lista e operador lógico ação (esse último para decidir o que retornará ao usuário)
contador = 1
índice = 0
#Declarou-se ação como falsa por questão de escolha
ação = False
#Estrutura de repetição para analisar cada elemento da lista
while contador <= len(teste):
    #Comparando o primeiro elemento como o último
    if teste[índice] == teste[len(teste) - contador]:
        #Se satisfeita a condição, aumenta-se o índice para analisar o proximo elemento e o contador para comparar esse elemento com o de índice (len(teste - contador)) e  para contar um elemento da lista já analisado
        índice += 1
        contador += 1
        #Declara-se ação como Verdadeira
        ação = True
    #Se a condição não for satisfeita, ação retorna como falsa e a estrutura de repetição é encerrada
    else: 
        ação = False
        break
#Se, após a estrutura de repetição cessar, ação continuar como verdadeira, retorna-se ao usuário que o número digitado é palíndromo
if ação == True:
    print("O número %s é palíndromo." % número)
#Se não (se ação continuar como falsa), retorna-se ao usuário que o número digitado não é palíndromo
else:
    print("O número %s não é palíndromo." % número)

#Ainda precisa aplicar restrição a entrada de dados, pois strings que começam com 0 podem furar o código. Exemplo: 090 não é palíndromo, apesar do código acima aceitar que é.

        
    