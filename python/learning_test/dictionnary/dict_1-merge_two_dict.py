# this trick merge 2 dictionnary and keep the biggest value if the same key is twice

x = {'a': 1, 'b':2}
y = {'b': 8, 'c':9}

z = x | y

print(z)