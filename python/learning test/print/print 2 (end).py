# l'exemple qui suit est la suite de Fibonacci

# le end en argument dans la fonction print permet
# de remplacer le changement de ligne par defaut 
# a la fin du print par autre chose (ou un caractere)

a, b, c = 1, 1, 1
while c < 11:
    print(b, end = " ")
    a, b, c = b, a + b, c + 1