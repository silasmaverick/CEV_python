#desafio 8
#conversor de metros para centimetros e milímetros
m = float(input('Digite a quantidade em metros: '))
c = m*100
ml = m*1000
print(f'{m} metros equivale a {c} centímetros e {ml} milímetros')

#desafio 9
#tabuada de um número
n = int(input('Digite um número: '))
print(f'tabuada do {n}: ')
for x in range(1,11):
    print(f'{n} x {x} = {(n*x)}')

# desafio 10
# conversor de real para dolar
real = int(input('Digite a quantidade de reais: '))
dolar = 5.42
print(f'Seus reais equivalem à: {(real / dolar):.2f}')



