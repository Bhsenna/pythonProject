"""
Criar um algoritmo que receba 4 notas e o nome do aluno,
Usar os seguintes critérios:
Nota entre 5 e 7 = Exame
Nota entre 7 e 9 = Aprovado
Nota entre 9 e 10 = Aprovado⭐⭐
Nota 10 = SUPER APROVADO
Nota entre 3 e 5 = Volte 2 casas e tente novamente
Nota entre 0 e 3 = HOJE NÃO, FARO
"""

nome = input('Insira seu nome: ')
n1 = int(input('Digite a nota 1: '))
n2 = int(input('Digite a nota 2: '))
n3 = int(input('Digite a nota 3: '))
n4 = int(input('Digite a nota 4: '))

media = (n1+n2+n3+n4)/4

if media == 10:
    print(f'{nome} foi ⭐⭐⭐SUPER APROVADO⭐⭐⭐')
elif media >= 9:
    print(f'{nome} foi ⭐APROVADO⭐')
elif media >= 7:
    print(f'{nome} foi Aprovado')
elif media >= 5:
    print(f'{nome} está em EXAME')
elif media >= 3:
    print(f'{nome}, volte 2 casas e tente novamente')
else:
    print('HOJE NÃO, FARO')