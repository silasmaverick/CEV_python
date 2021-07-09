a = float(input('Digite o comprimento da reta A: '))
b = float(input('Digite o comprimento da reta B: '))
c = float(input('Digite o comprimento da reta C: '))
tipo = 'a'

if a == b and a == c:
    tipo = 'Equilátero'
elif a == b and a != c or a == c and a != b or b == c and b != a:
    tipo = 'Isósceles'
else:
    tipo = 'Escaleno'

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print(f'Pode-se formar um triângulo {tipo}')

else:
    print ('Não pode se formar um triângulo')
