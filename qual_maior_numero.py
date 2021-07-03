n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

#verificando o maior
if n1 > n2 and n1 > n3:
    print (f'O maior número é o número {n1}')
elif n2 > n1 and n2 > n3:
    print (f'O maior número é o número {n2}')
else :
    print(f'O maior número é o número {n3}')
# verificando o menor
#------------------------------
if n1 < n2 and n1 < n3:
    print (f'O menor número é o número {n1}')
elif n2 < n1 and n2 < n3:
    print (f'O menor número é o número {n2}')
else :
    print(f'O menor número é o número {n3}')

# pode-se definir menor = a. if b<a and b<C