nome = input('Digite o seu nome: ')
n1 = int(input('Digite nota 1: '))
n2 = int(input('Digite nota 2: '))
n3 = int(input('Digite nota 3: '))
n4 = int(input('Digite nota 4: '))
media = (n1+n2+n3+n4)/4

if media > 10:
    print(f'{nome}, você quebrou o sistema')
elif media >= 7:
    print(f'{nome}, você foi APROVADO')
elif media >= 5:
    print(f'{nome}, você ficou em EXAME')
else:
    print(f'{nome}, você não estudou o suficiente')
