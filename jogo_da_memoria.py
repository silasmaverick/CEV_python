#%%
##exercicio 28 jogo de adivinhação
from random import randint
from time import sleep
print('=-'*30)
print('Vou pensar em um número entre 1 e 7. Tente adivinhar...')
print('=-'*30)
pc = randint(1, 7)
print('Pensando.....')
sleep(2)
print('Já pensei!!')
print('=-'*30)
n = int(input('Em que número eu pensei? '))
print('.'*5)
sleep(2)
cont = 1

if n == pc:
    print('Você ADIVINHOU!!!')
    print(f'O número correto é: {pc}')
    print(f'Você precisou de {cont} tentativas')

if n != pc:
    while n != pc:               
        print('Você errou!! Não foi dessa vez!!! =(')
        t = int(input('Tente novamente... Digite um número: '))
        n = t
        cont +=1
        print('.'*5)
        sleep(1)
        
        

if n == pc:
    print('Você ADIVINHOU!!!')
    print(f'O número correto é: {pc}')
    print(f'Você precisou de {cont} tentativas')



# %%
