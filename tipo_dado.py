n = input('Digite algo: ')
print(type(n))
print('É alfanumérico?', (n.isalpha()))
print('É numérico?', (n.isnumeric()))
print('É imprimivel?', (n.isprintable()))
print('É um decimal?', (n.isdecimal()))
print('Está capitalizada?', (n.isupper()))
