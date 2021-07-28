#ex 46- Faça um programa que mostre na tela uma contagem regressiva para o
#estouro de fogos de artificio, indo de 10 até 0
#com uma pausa de 1 segundo entre eles///
#%%
from time import sleep


for n in range (10,0, -1):
    print(n)
    sleep(1)
# %%
# crie um programa que mostre 
# na tela todos os numeros pares que estao entre 1 e 50
for n in range (2,51, 2):
    print(n)
# %%
#faca um programa que calcule a soma entre todos
#os numeros impares que sao multiplos
#de tres e que se encontram no intervalo de 1 até 500

#%%
soma = 0
for n in range (1,501, 2):
    if n%3 == 0:
        soma += n 

print(soma)
#%%

a = int(input('Qual número você quer taboada? '))

for x in range (1,11):
    tab = a * x 
    print (f'{a} x {x} = {tab}')
    
# %%
#desenvolva um progama que leia seis numeros inteiros e 
# mostre a soma apenas daqueles
# que forem pares. se o valor for impar desconsidere-o

soma = 0
for n in range (1, 7):
    num = int(input(f'Digite o numero {n}: '))
    if num % 2 == 0:
        soma += num

print(soma)




# %%
#desenvolva um programa que leia o primeiro termo e a razao de uma
#  p.a. 
#No final, mostre os 10 primeiros termos dessa progressão

pt = int(input('Digite a primeiro termo da progressao aritimética: '))
razao = int(input('Digite a razao da progressão aritimética: '))
p = pt + (10-1) * razao
for n in range (pt, p+razao, razao):
    print(n)





# %%
#52 - faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo 

num = int(input('Digite um número: '))
cont = 0 
for n in range (1, num + 1):
    if  num % n == 0:
        cont += 1

if cont == 2:
    print('O número é primo')
else:
    print('O número não é primo')

print(f'O número foi divisível por {cont} números')
    
  
# %%
#crie um programa que leia o ano de nascimento de sete pessoas.
# no final mostre quantas pessoas ainda não atingiram a maioridade
# e quantas ja sao maiores 21 anos
from datetime import date
cmaior = 0
cmenor = 0
hoje = date.today().year

for n in range (1,8):
    nasc = int(input(f'Digite o ano de nascimento {n} '))
    idade = hoje - nasc
    if idade < 21:
        cmenor += 1
    else:
        cmaior += 1
        
print(f' {cmenor} pessoas são menores de idade')
print (f' {cmaior} pessoas são maiores de idade')




# %%
#55- faça um programa que leia o peso de cinco pessoas,
#  no final mostre qual foi o maior e o menor peso lido.
maior = 0
menor = 0
for n in range (1,6):
    peso = int(input('Digite o peso: '))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso <= menor:
            menor = peso
    
           
print(maior)
print(menor)


# %%
#%%Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
#a média de idade do grupo, qual é o nome do homem mais velho 
# e quantas mulheres têm menos de 20 anos.
nomeh =''
homem = 0
mulher = 0 
soma_idade = 0
 

for n in range (1,5):
    nome = str(input(f'digite o nome da pessoa nº {n}'))
    idade = int(input(f'digite a idade da pessoa nº{n}'))
    soma_idade += idade
    media = (soma_idade / 4) 
    sexo = int(input(f'digite o sexo da pessoa nº {n}: \n[1]MASCULINO --------[2]FEMININO: '))
    
    if sexo==1:
        homem +=1 
        maior = 0
        menor = 0
        for n in range(1,5):
            if n == 1:
                maior = idade
                menor = idade
                nomeh = nome
            else:
                if idade > maior:
                    maior = idade
                    nomeh = nome
                if idade <= menor:
                    menor = idade

    if sexo==2:
        if idade < 20:
            mulher += 1
        
    


print(f' A média de idade é {media}')
print(f' O nome do homem mais velho é:{nomeh}')
if mulher > 0:
    print(f' A quantidade de mulheres com idade inferior a 20 anos é {mulher}')
else:
    print('não existe mulheres com essa idade')


