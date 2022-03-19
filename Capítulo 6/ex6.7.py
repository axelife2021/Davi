expressão_string = input("Digite uma expressão com parênteses: ")
expressão = []
expressão.extend(expressão_string)
chars = len(expressão)
if expressão.pop(n) == "(":
    chars += 1
    expressão.append("-")
if expressão.pop(n) == ")":
