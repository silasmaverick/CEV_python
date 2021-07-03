a = float(input('Digite a reta A: '))
b = float(input('Digite a reta B: '))
c = float(input('Digite a reta C: '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Pode-se formar um triângulo')
else:
    print ('Não pode se formar um triângulo')
