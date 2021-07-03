salario = float(input('Digite seu salário: '))
if salario > 1250:
    print(f'O seu salário aumentará 10% passando de R${salario:.2f} para R${(salario*10/100)+salario:.2f}')
else:
    print(f'O seu salário aumentará 15% passando de R${salario:.2f} para R${(salario*15/100)+salario:.2f} ')
