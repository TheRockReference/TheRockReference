
# Ceci est un exercice du livre Apprendre a programmer avec python 3 de Gerard Swinnen

# Exercice 4.4
# Écrivez un programme qui affiche une suite de 12 nombres dont chaque terme soit
# égal au triple du terme précédent.

i, j = 1, 1
while j < 13:
    print(i, end=' ')
    i, j = i * 3, j + 1