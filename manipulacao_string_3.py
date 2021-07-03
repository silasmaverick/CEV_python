frase = str(input('Digite uma frase: ')).lower().strip()
print(f'A letra "A" apareçe {frase.count("a")} vezes na frase')
print(f'A primeira letra "A", apareceu na posição {frase.find("a")+1}')
print(f'A ultima letra "A", apareceu na posição {frase.rfind("a")+1}')

n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[len(nome)-1]} ')
