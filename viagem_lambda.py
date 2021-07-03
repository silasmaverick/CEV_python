distancia = float(input('Qual a distância em km? '))
preço = distancia*0.5 if distancia<=200 else distancia*0.45
print(f'O preço da passagem será de R${preço:.2f}')

#if distancia < 200:
 #   print(f'O preço da passagem será R${(distancia*0.5):.2f}')
#else:
 #   print(f'O preço da passagem será de R$ {(distancia*0.45):.2f}')

