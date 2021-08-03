#%%crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuario digitar o valor 999 
# que é a condição de parada.
#  No final, mostre quantos números foram digitados 
#e qual foi a soma entre eles desconsiderando o flag

cont= 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont +=1
    soma += n

print(f'foram digitados {cont} números')
print(f'A soma dos números foi de: {soma}')

#%%
#69 - crie um programa que leia a idade e o#  sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#  No final, mostre:
#A) - quantas pessoas tem mais de 18 anos
#B) - quantos homens foram cadastrados
#C) - quantas mulheres tem menos de 20 anos
contid = 0
contman = 0
contwom = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o Sexo [M] Masculino ou [F] Feminino').upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo inválid. Digite o Sexo [M] Masculino ou [F] Feminino').upper()
    if idade > 18:
        contid += 1
    if sexo == 'M':
        contman += 1
    if sexo == 'F' and idade < 20:
        contwom +=1
    n = int(input('Deseja continuar? [1]SIM -- [2]NÃO'))
    if n == 2:
        break

print(f'foram cadastradas {contid} pessoas maiores de 18 anos')
print(f'foram cadastrados {contman} homens')
print(f'foram cadastradas {contwom} mulheres menores de 20 anos')


# %%
#70 - crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar. No final mostre:
#A) qual é o total gasto na compra.
#B)Quantos produtos custam mais de R$1000
#C)Qual é o nome do produto mais barato. 
tot = 0
cont_mil = 0
menor_nome = ''
menor = 0
while True:
    preco = float(input('Digite a preço: R$ '))
    if menor == 0:
        menor = preco
        menor_nome = nome
    nome = input('Digite nome do produto')
    tot += preco
    if preco < menor:
        menor_nome = nome
        menor = preco
        
    if preco > 1000:
        cont_mil += 1 
    n = int(input('Deseja continuar? [1]SIM -- [2]NÃO'))
    if n == 2:
        break
 
print(f'O total gasto foi de R${tot:.2f}')
if cont_mil == 1:
    print(f'{cont_mil} produto custa acima de R$1000,00')
elif cont_mil > 1:
    print(f'{cont_mil} produtos custam acima de R$1000,00')
print(f'O produto {menor_nome} é o produto mais barato custando {menor:.2f}')

# %%
