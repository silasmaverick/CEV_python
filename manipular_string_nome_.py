# 22 - manipulando strings
nome = str(input('Digite seu nome:')).strip()
print(nome.title())
print(f'seu nome tem Silva? {("Silva" in nome) }')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')

