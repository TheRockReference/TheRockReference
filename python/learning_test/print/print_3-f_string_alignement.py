
# Ceci est un exercice du livre Apprendre a programmer avec python 3 de Gerard Swinnen

# Exercice 4.3
# Ecrivez un programme qui affiche une table de conversion de sommes d"argent exprimees
# en euro, en dollars canadiens. La progression des sommes de la table sera "geometrique",
# comme dans l'exemple ci-dessous : 

# 1 euro = 1.65 dollars
# 2 euros = 3.30 dollars
# 4 euros = 6.60 dollars
# 8 euros = 13.20 dollars
# (arrêtez-vous à 16384 euros)


#You can use the :>, :< or :^ option in the f-format to left align, right align or center align the text that you want to format.
print("sans formattage")
i = 1
while i < 16384:
    
    print(f"{i} dollars = {i * 1.65} euros")
    i = i * 2
    

print("\n")
    

print("aligné à droite")
i = 1
while i < 16384:
    
    print(f"{i:>12} dollars = {i * 1.65:>12} euros")
    i = i * 2
    

print("\n")


print("aligné à gauche")
i = 1
while i < 16384:
    
    print(f"{i:<12} dollars = {i * 1.65:<12} euros")
    i = i * 2
        

print("\n")


print("centré")
i = 1
while i < 16384:
    
    print(f"{i:^12} dollars = {i * 1.65:^12} euros")
    i = i * 2