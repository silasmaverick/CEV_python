from random import randint
from time import sleep

pedra = 1
papel = 2
tesoura = 3


print('=-'*30)

print('JOKENPÔ')

print('=-'*30)

pc = randint(1, 3)

print('Qual a sua jogada \n(1)PEDRA \n(2)PAPEL \n(3)TESOURA')
print('=-'*30)

n = int(input(' '))

if n not in range (1,4):
    print('Jogada inválida')
else:
    if n == pc:
        print('Jogo empatado... Ambos escolheram o mesmo!')

    elif n == 1:
        if pc == 2:
            print('.'*5)
            sleep(1)
            print('Você perdeu! \nO computador escolheu papel... que embrulhou sua pedra!!')
        else:
            print('.'*5)
            sleep(1)
            print('Você ganhou! \nO computador escolheu tesoura... sua pedra acabou com ela!!')

    elif n ==2:
        if pc == 1:
            print('.'*5)
            sleep(1)
            print('Você ganhou! \nO computador escolheu pedra... você embrulhou a pedra dele e levou pra casa!!')
        else:
            print('.'*5)
            sleep(1)
            print('Você perdeu! \nO computador escolheu tesoura... seu papel foi picotado!!')

    else:
        if pc == 1:
            print('.'*5)
            sleep(1)
            print('Você perdeu! \nO computador escolheu pedra... sua tesoura foi destruida!!')
        else:
            print('.'*5)
            sleep(1)
            print('Você ganhou! \nO computador escolheu papel... seu sua tesoura picotou ele!!')