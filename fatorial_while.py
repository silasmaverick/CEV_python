#%%faça um programa que leita um numero qualquer e mostre o seu fatorial
n = int(input('Digite um número'))
produto = 1
for x in range (n,0,-1):
 
    produto = produto * x   
print(produto)    


# %%
n = int(input('Digite um número: '))
produto = 1 

while n > 0:
    produto = produto * n
    n = n-1

print(produto)