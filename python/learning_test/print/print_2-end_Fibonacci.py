# l'exemple qui suit est la suite de Fibonacci

# c'est une suite de nombre dont chaque terme est égal à la somme
# des 2 termes précédents.

# le end en argument dans la fonction print permet
# de remplacer le changement de ligne par defaut 
# a la fin du print par autre chose (ou un caractere)



a, b, c = 1, 1, 1       # a et b servent au calculs des termes successifs
while c < 11:           # c est un simple compteur
    print(b, end = " ")
    a, b, c = b, a + b, c + 1