num = input('\x1b[38;5;3mDigite um número: ')
while type(num) != int:
    try:
        num = int(num)
    except:
        print('Número inválido, tente novamente')
        num = input('Digite um número: ')

print(f'Números ímpares: ', end='')
for i in range(num+1):
    if i % 2:
        print(i, end=' ')