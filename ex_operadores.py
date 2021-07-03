#desafio 5
n = int(input('Digite um número: '))
print('O número digitado é {}'.format(n))
print('O número antecessor é: {} e o número sucessor é: {}'.format(n-1, n+1))

#desafio 6
##algoritmo para que mostre o dobro triplo e raiz quadrada de um número
n =int(input('Digite um número: '))
d = float(n*2)
t = float(n*3)
rq = float(n ** (1/2))

print(f'O numéro digitado é {n}')
print(f'O seu dobro é: {d}, o seu triplo é {t}, sua raíz quadrada é: {rq} ')

#desafio 7
#duas notas de um aluno calcule e mostre a média
n1 = float(input('Digite a nota 01: '))
n2 = float(input('Digite a nota 02: '))
media = (n1+n2)/2
print(f'A média do aluno é: {media}')


#desafio 12
#faça um programa que leia um preço e calcule o novo preço com 5% de desconto
preco = float(input('Digite o preço do produto: '))
calc = preco - ((preco*5)/100)
desconto = print(f' O preço do produto com desconto é: {calc}')

#desafio 13
#faça um programa leia um salário e calcule 15% de aumento
salario = float(input('Digite seu salário: '))
cals = salario +((salario*15)/100)
print(f'Seu salário com aumento de 15% é: {cals}')
