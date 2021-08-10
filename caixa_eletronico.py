#%%
#Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado.(int) e programa vai informar quantas cédulas de cada valor serão entregues.
#Considere que o caixa possui células de 50, 20, 10 e 1
print('='*40)
print('$-BANCO LINO-$')

n = int(input('Digite um valor para saque: R$ '))
inicio = n
print('='*40)


cedu50 = 0
cedu20 = 0 
cedu10 = 0
cedu01 = 0 
resto = 1

while resto > 0:
    if resto == 0:
        break
    if n % 50 == 0:
        cedu50 = n // 50 
        resto = 0 
    if n % 50 >=1:
        cedu50 = n // 50
        resto = n % 50
        n = resto
        
    if n % 20 == 0:
        cedu20 = n // 20
        resto = 0
    if n % 20 >= 1:
        cedu20 = n // 20
        resto = n % 20
        n = resto
        
    if n % 10 == 0:
        cedu10 = n // 10
        resto = 0    
    if n % 10 >= 1:
        cedu10 = n // 10
        resto = n%10
        n = resto
        
    if resto !=0:     
        if n % 1 == 0:
            cedu01 = n // 1
            resto = 0
 
print(f'O valor solicitado foi R$ {inicio}')
if cedu50 > 0:           
    print(f'Será impresso {cedu50} nota(s) de R$50')
if cedu20 > 0:
    print(f'Será impresso {cedu20} nota(s) de R$20')
if cedu10 > 0:
    print(f'Sera impreso {cedu10} nota(s) de R$10')
if cedu01 > 0:    
    print(f'Sera impreso {cedu01} nota(s) de R$1')
print('='*40)
print('OBRIGADO POR UTILIZAR E VOLTE SEMPRE!')






        






# %%
