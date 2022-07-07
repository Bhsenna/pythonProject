rep = 's'
while rep == 's':
    num = input('Escolha um número: ')
    if num.lstrip('-').isdigit():
        num = int(num)

    tab = 1
    while tab <= 10:
        print(f'{num} x {tab} = {num * tab}')
        tab += 1

    rep = input('Quer outra tabuada? (S ou N)\n').lower()