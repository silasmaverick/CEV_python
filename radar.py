vel = int(input('Informe a velocidade do carro: '))

if vel > 80:
    print('A velocidade máxima permitida é de 80km/h')
    excesso = vel-80
    multa = float(excesso*7)
    print(f'Você foi multado!!. O valor a ser pago será R${multa:.2f}')
else:
    print('Você não foi multado, continue com segurança')

#par ou impar

n = float(input('Digite num:' ))
if n % 2 == 0:
    print('O número é par')
else:
    print('O número é impar')