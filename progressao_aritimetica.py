#%%leia o primeiro termo e a razao de uma pa,
# mostrando os 10 primeiros termos da progressão usando a estrutura while
#Melhore  perguntando para o usuário se ele quer mostrar mais alguns termos.
#  O programa encerrará quando ele disser que quer mostrar 0 termos.
print('\n')
print('--------PROGRESSÃO ARITMÉTICA ---------')
print('.........aguardando os termos..........')
print('\n')
pt = int(input('Digite o primeiro termo: '))
print('\n')
razao = int(input('Digite a razão: '))
cont = 1 
b = 11
qst= 1

while qst != 0:
    while cont < b:
        print(pt)  
        pt += razao
        cont += 1
    qst = int(input('Você quer adicionar mais termos? Se sim, digite a quantidade ou [0] para sair: '))
    b = qst + b
print('Obrigado.... Saindo....')


#%%crie um programa que leia vários números inteiros pelo teclado.
#  O programa só vai parar quando o usuario digitar o valor 999. # Que é a condição de parada.
#  No final, mostre quantos números foram digitados e qual foi a soma entre eles 
# desconsiderando o flag
cont = 0
soma = 0
n = 0

while n != 999:
    n = int(input('Digite um número ou 999 para sair: '))
    if n != 999:
        
        cont +=1
        soma += n

print(soma)
print(cont)
# %%
#crie um programa que leia vários números inteiros pelo teclado.
# No final da execucao, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
cont=0
soma = 0
 
n = int(input('Digite um número ou digite 0 para sair: '))
maior = n
menor = n
if n != 0:
    while n!= 0:           
        if n != 0:
            soma += n
            cont +=1
            if n > maior:
                maior = n
            if n < menor :
                menor = n
            n = int(input('Digite um número ou digite 0 para sair: '))
        else:
            
            print('Obrigado saindo')
else:
    print('Obrigado saindo....')
print(f'A soma dos números digitados é {soma}')
print(f'O menor número digitado foi {menor}')
print(f'O maior número digitado foi {maior}')
if soma != 0:
    print(f'A média foi de {(soma/cont):.2f}')
    




# %%
