from random import choice
from time import sleep


def getInt(inp):
    num = input(inp).strip()
    while type(num) != int:
        try:
            num = int(num)
        except:
            num = input(inp)
    return num


def getFloat(inp):
    num = input(inp).strip().replace(',', '.')
    while type(num) != float:
        try:
            num = float(num)
        except:
            num = input(inp).strip().replace(',', '.')
    return num


def getMeds(ld):
    return getInt(f'Informe o comprimento do(a) {ld}:\n')


def checkTry(lisMed):
    lisMed.sort()
    if lisMed[0] + lisMed[1] < lisMed[2]:
        return False
    else:
        return True


def triangType(lisMed):
    if lisMed[0] == lisMed[1] == lisMed[2]:
        return 'Equilátero'
    elif lisMed[0] == lisMed[1] != lisMed[2] or lisMed[1] == lisMed[2] != lisMed[0] or lisMed[0] == lisMed[2] != lisMed[1]:
        return 'Isosceles'
    else:
        return 'Escaleno'


def letCount(letra, string):
    cont = 0
    for i in range(len(string)):
        if string[i] == letra:
            cont += 1
    return cont


def rever(num):
    if num.isdigit():
        return ''.join(sorted(num, reverse=True))
    else:
        return 'Não é um número'


def getDig(num):
    if type(num) == int or num.isdigit():
        return len(str(num))
    else:
        return 'Não é um número'


def rps():
    a = getInt('[1] Pedra\n[2] Papel\n[3] Tesoura\n')
    while str(a) not in '123' and len(str(a)) != 1:
        a = getInt('[1] Pedra\n[2] Papel\n[3] Tesoura\n')
    if a == 1:
        return 'Pedra'
    elif a == 2:
        return 'Papel'
    elif a == 3:
        return 'Tesoura'


def rps_pc():
    a = choice(['Pedra', 'Papel', 'Tesoura'])
    return a


def rps_timer():
    sleep(1)
    print('JO', end='')
    sleep(2)
    print('KEN', end='')
    sleep(2)
    print('PO!')


def rps_game(p, c):
    if p == c:
        print(f'Empate! O jogador escolheu {p}, e o computador escolheu {c}')
        return 0
    elif p == 'Pedra' and c == 'Papel':
        print(f'Derrota! O jogador escolheu {p}, e o computador escolheu {c}')
        return 1
    elif p == 'Papel' and c == 'Tesoura':
        print(f'Derrota! O jogador escolheu {p}, e o computador escolheu {c}')
        return 1
    elif p == 'Tesoura' and c == 'Pedra':
        print(f'Derrota! O jogador escolheu {p}, e o computador escolheu {c}')
        return 1
    else:
        print(f'Vitória! O jogador escolheu {p}, e o computador escolheu {c}')
        return 2