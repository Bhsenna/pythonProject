rep = 's'
while rep == 's':
    num = input('Escolha um número: ')
    if num.lstrip('-').isdigit():
        num = int(num)

    fat, uwu = 1, 1
    while fat <= num:
        uwu = fat * uwu
        fat += 1
    print(f'O fatorial de {num} é igual a {uwu}')

    rep = input('Quer outro fatorial? (S ou N)\n').lower()