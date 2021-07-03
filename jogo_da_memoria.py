##exercicio 28 jogo de adivinhação
from random import randint
from time import sleep
print('=-'*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=-'*30)
pc = randint(0, 5)
print('Pensando.....')
sleep(2)
print('Já pensei!!')
print('=-'*30)
n = int(input('Em que número eu pensei? '))
print('.'*5)
sleep(3)
if n == pc:
    print('Você ADIVINHOU!!!')
else:
    print('Você errou!! Não foi dessa vez!!! =(')
    print(f'O número correto é: {pc}')
