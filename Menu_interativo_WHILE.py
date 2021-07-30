#%%
val = [1,2,3]
print(f'MENU DE OPERAÇÕES')
print('[1]SOMAR -----[2]MULTIPLICAR -----[3]MAIOR-----')
print('\n')
print('*'*50)
print('\n\n')
print('Digite os números e a operação desejada')

print('Aguardando Valores...')
print('\n')

a = int(input('Digite o primeiro valor: '))

print(f'Valor 1: {a}')
print('\n')
print('Escolhendo operação...')
print('[1]SOMAR -----[2]MULTIPLICAR -----[3]MAIOR-----')
print('\n')

e = int(input('Qual a sua escolha?: '))
while e not in val:
            e = int(input('Escolha inválida. Qual a sua escolha?'))

if e == 1: print('Operação de Soma')
elif e == 2: print('Operação Multiplicação')
elif e == 3: print('Operação Análise maior número')
print('\n')

b = int(input('Digite o segundo valor: '))
print(f'Valor 2: {b}')
print('\n')
print('*'*50)

while e != 5:
        
    if e == 1:
        
        print(f'A soma é {a+b}')
        print('\n')
        print('[1]SOMAR -----[2]MULTIPLICAR -----[3]MAIOR-----[4]NOVOS NÚMEROS-----[5]SAIR')
        e = int(input('Qual a sua escolha?: '))

    if e == 2:
        
        print('\n')
        print('*'*50)
        print(f'O produto é {a*b}')
        print('\n')
        print('[1]SOMAR -----[2]MULTIPLICAR -----[3]MAIOR-----[4]NOVOS NÚMEROS-----[5]SAIR')
        e = int(input('Qual a sua escolha?: '))
        
    if e == 3:
        
        print('\n')
        
        lst = {a,b}
        print(f'O Maior número é: {max(lst)}')
        print('\n')
        print('[1]SOMAR -----[2]MULTIPLICAR -----[3]MAIOR-----[4]NOVOS NÚMEROS-----[5]SAIR')
        e = int(input('Qual a sua escolha?': ))

    if e == 4:
        
        print('Novos números:')
        print('\n')
        print('*'*50)
        print('Aguardando Valores...')
        a = int(input('Digite o primeiro valor: '))
        print(f'Valor 1: {a}')

        print('Escolhendo operação...')
        print('[1]SOMAR -----[2]MULTIPLICAR -----[3]MAIOR-----')
        e = int(input('Qual a sua escolha?: '))
        while e not in val:
            e = int(input('Escolha inválida. Qual a sua escolha?: '))

        b = int(input('Digite o segundo valor: '))
        print(f'Valor 2: {b}')
        print('\n')

    if e==5:
        print('\n')
        print('*'*50)
        print('---Saindo....---')

# %%
