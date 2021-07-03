#desafio 11
#faça um programa que leia a largura e a altura de uma parede, calcule sua área
#e quantidade de tinta para pintar, considerando que cada litro pinte 2metros2
altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))
area = altura*largura
latas = int(area//2 + 1)
print(f'A área a ser preenchida é {area:.2f} m2, sendo necessário o uso de {latas} latas de tinta para executar o serviço. ')