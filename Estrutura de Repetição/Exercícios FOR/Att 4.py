print('\x1b[38;5;3mTABUADAS!\n')

rep = input('Deseja ver uma tabuada? [S ou N]\nResposta: ').upper().strip()
while rep not in ["S", "N"]:
    rep = input('\nDeseja ver uma tabuada? [S ou N]\nResposta: ').upper().strip()
while rep == 'S':
    num = input('\nTabuada de: ')
    while type(num) != int:
        try:
            num = int(num)
        except:
            print('Número inválido, tente novamente')
            num = input('Tabuada de: ')
    print()
    for i in range(10):
        print(f'{num} x {i+1} = {num * (i+1)}')
    rep = input('\nDeseja ver uma tabuada? [S ou N]\nResposta: ').upper().strip()
    while rep not in ["S", "N"]:
        rep = input('\nDeseja ver uma tabuada? [S ou N]\nResposta: ').upper().strip()