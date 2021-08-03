# %%faça um programa que mostre a tabuada de vários numeros,
#  um de cada vez para cada valor digitado pelo usuario. 
#O programa será interrompido quando o número solicitado for negativo
print('TABOADA\n')

while True:
    n = int(input('Digite um número inteiro positivo para ver sua taboada: '))
    if n <= 0:
        break
    print(f'taboada do {n}')
    for x in range (1,11):
        prd = x * n       
        print(prd,'', end='|')
    print('\n')

print('\nObrigado')
