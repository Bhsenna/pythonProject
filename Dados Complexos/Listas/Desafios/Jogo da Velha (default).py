from random import choice
cont = 0
pc = 0
pl = 0
em = 0


def title():
    print(25 * '\33[32;1m=')
    print('JOGO DA VELHA'.center(25))
    print(25 * '=' + '\33[0m')


def tabuleiro():
    print(f'''\n{pos[7]}|{pos[8]}|{pos[9]}
-+-+-
{pos[4]}|{pos[5]}|{pos[6]}
-+-+-
{pos[1]}|{pos[2]}|{pos[3]}''')


def referencia():
    print(f'''\n{ref[7]}|{ref[8]}|{ref[9]}
-+-+-
{ref[4]}|{ref[5]}|{ref[6]}
-+-+-
{ref[1]}|{ref[2]}|{ref[3]}''')


def pecas(con):
    if con % 2:
        jog = 'X'
        cpu = 'O'
    else:
        jog = 'O'
        cpu = 'X'
    return jog, cpu


def player(jog):
    referencia()
    jogada = input('\33[38;5;45mEscolha a posição que deseja jogar\33[0m\n')
    while type(jogada) != int:
        try:
            jogada = int(jogada)
            if pos[jogada] != ' ':
                print('Posição inválida, tente novamente')
                jogada = input('\33[38;5;45mEscolha a posição que deseja jogar\33[0m\n')
        except:
            print('Posição inválida, tente novamente')
            jogada = input('\33[38;5;45mEscolha a posição que deseja jogar\33[0m\n')
    while pos[jogada] == ' ':
        if str(jogada) not in '123456789':
            print('Posição inválida, tente novamente')
            jogada = input('\33[38;5;45mEscolha a posição que deseja jogar\33[0m\n')
        else:
            pos[jogada] = jog[0]
            ref[jogada] = jog[0]


def copiatab(tabu):
    copia = []
    for i in tabu:
        copia.append(i)
    return copia


def computador(cpu):
    done = False
    while not done:
        for i in range(1, 10):
            cop = copiatab(pos)
            if pos[i] == ' ':
                cop[i] = cpu[1]
                if venceu(cop, pecas(cont), 'c'):
                    pos[i] = cpu[1]
                    ref[i] = cpu[1]
                    return
        for i in range(1, 10):
            cop = copiatab(pos)
            if pos[i] == ' ':
                cop[i] = cpu[0]
                if venceu(cop, pecas(cont), 'p'):
                    pos[i] = cpu[1]
                    ref[i] = cpu[1]
                    return
        if pos[7] == ' ' or pos[9] == ' ' or pos[1] == ' ' or pos[3] == ' ':
            a = [7, 9, 1, 3]
            b = choice(a)
            if not pos[b] != ' ':
                pos[b] = cpu[1]
                ref[b] = cpu[1]
                done = True
        elif pos[5] == ' ':
            pos[5] = cpu[1]
            ref[5] = cpu[1]
            done = True
        else:
            a = [8, 4, 6, 2]
            b = choice(a)
            if not pos[b] != ' ':
                pos[b] = cpu[1]
                ref[b] = cpu[1]
                done = True


def venceu(bo, pec, tur):
    if tur == 'p':
        le = pec[0]
    else:
        le = pec[1]
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # topo
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # meio
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # baixo
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # esquerda
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # meio
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # direita
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def empate():
    for i in range(1, 10):
        if pos[i] == ' ':
            return True


title()
while cont < 5:
    turn = 1
    cont += 1
    pos = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ref = ['0', '\33[32;1m1\33[0m', '\33[32;1m2\33[0m', '\33[32;1m3\33[0m', '\33[32;1m4\33[0m', '\33[32;1m5\33[0m', '\33[32;1m6\33[0m', '\33[32;1m7\33[0m', '\33[32;1m8\33[0m', '\33[32;1m9\33[0m']
    while True:
        if not turn == 1:
            tabuleiro()
        player(pecas(cont))
        turno = 'p'
        if venceu(pos, pecas(cont), turno):
            tabuleiro()
            print('\33[38;5;46mParabéns, você venceu!\33[0m')
            pl += 1
            break
        elif not empate():
            tabuleiro()
            print('\33[38;5;226mO jogo deu velha!\33[0m')
            em += 1
            break
        computador(pecas(cont))
        turno = 'c'
        if venceu(pos, pecas(cont), 'turno'):
            tabuleiro()
            print('\33[38;5;196mOh não, o Computador venceu!\33[0m')
            pc += 1
            break
        elif not empate():
            tabuleiro()
            print('\33[38;5;226mO jogo deu velha!\33[0m')
            em += 1
            break
        turn += 1
print(f'\nO jogo terminou, você venceu {pl} vezes, o computador venceu {pc} vezes, e houve {em} empates')