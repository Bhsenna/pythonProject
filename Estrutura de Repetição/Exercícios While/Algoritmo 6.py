rep = 's'
while rep == 's':
    numL = input('Insira os seus números: ').split()

    cont = 0
    while cont < len(numL):
        if numL[cont] == '0':
            numL.pop(cont)
        elif numL[cont].lstrip('-0').isnumeric():
            numL[cont] = int(numL[cont])
            cont += 1
        else:
            numL.pop(cont)

    cont = 0
    neg, i1, i2, i3, i4 = 0, 0, 0, 0, 0
    while cont < len(numL):
        if numL[cont] < 0:
            print(f'O {cont + 1}° número é negativo!')
            neg += 1
            break
        elif 0 <= numL[cont] <= 25:
            i1 += 1
        elif 26 <= numL[cont] <= 50:
            i2 += 1
        elif 51 <= numL[cont] <= 75:
            i3 += 1
        elif 76 <= numL[cont] <= 100:
            i4 += 1
        cont += 1

    if not neg:
        print(f'Dos {len(numL)} números, {i1} eram entre 0 e 25, {i2} eram entre 26 e 50, {i3} eram entre 51 e 75, e {i4} eram entre 76 e 100')
    rep = input('\nQuer ver outra lista? (S ou N)\n').lower()