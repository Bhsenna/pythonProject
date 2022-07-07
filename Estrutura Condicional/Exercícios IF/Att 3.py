# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#  para homens: (72.7 * altura)         1,85 * 72.7 = 134,5
#  para mulheres: (62.1 * altura)       1,60 * 62,1 = 99,36

sex = input('Informe o seu sexo (M/F): ').lower()
alt = int(input('Informe a sua altura (cm): ')) / 100

if sex == 'm':
    print(f'Seu peso ideal é entre {(20.7 * alt ** 2):.2f}kg e {(26.4 * alt ** 2):.2f}kg')
elif sex == 'f':
    print(f'Seu peso ideal é entre {(19.1 * alt ** 2):.2f}kg e {(25.8 * alt ** 2):.2f}kg')
else:
    print(f'Seu peso ideal é [DADOS EXPURGADOS]')