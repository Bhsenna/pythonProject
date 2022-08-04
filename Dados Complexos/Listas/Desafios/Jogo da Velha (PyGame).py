from random import choice
from time import sleep
import pygame
cont = 0
pc = 0
pl = 0
em = 0

pygame.init()
white = (255, 255, 255)
screen = pygame.display.set_mode((360, 360))
pygame.display.set_caption('Jogo da Velha - Por: Hazime')

board = pygame.image.load(r'1Pzpe.png')
x = pygame.image.load(r'tic-tac-toe_39453 (1).png')
o = pygame.image.load(r'tic-tac-toe_39453 (2).png')
X = pygame.image.load(r'tic-tac-toe_39453 (3).png')
O = pygame.image.load(r'tic-tac-toe_39453 (4).png')
font = pygame.font.SysFont('None', 36)
screen.fill(white)
screen.blit(board, (0, 0))


def pecas(con):
    if con % 2:
        jog = 'X'
        cpu = 'O'
    else:
        jog = 'O'
        cpu = 'X'
    return jog, cpu


def player(jog):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pos()[0] < 112:
                    if pygame.mouse.get_pos()[1] < 112:
                        if pos[7] != ' ':
                            continue
                        else:
                            pos[7] = jog[0]
                            return
                    elif 128 < pygame.mouse.get_pos()[1] < 233:
                        if pos[4] != ' ':
                            continue
                        else:
                            pos[4] = jog[0]
                            return
                    elif 248 < pygame.mouse.get_pos()[1] < 360:
                        if pos[1] != ' ':
                            continue
                        else:
                            pos[1] = jog[0]
                            return
                elif 128 < pygame.mouse.get_pos()[0] < 233:
                    if pygame.mouse.get_pos()[1] < 112:
                        if pos[8] != ' ':
                            continue
                        else:
                            pos[8] = jog[0]
                            return
                    elif 128 < pygame.mouse.get_pos()[1] < 233:
                        if pos[5] != ' ':
                            continue
                        else:
                            pos[5] = jog[0]
                            return
                    elif 248 < pygame.mouse.get_pos()[1] < 360:
                        if pos[2] != ' ':
                            continue
                        else:
                            pos[2] = jog[0]
                            return
                elif 248 < pygame.mouse.get_pos()[0] < 360:
                    if pygame.mouse.get_pos()[1] < 112:
                        if pos[9] != ' ':
                            continue
                        else:
                            pos[9] = jog[0]
                            return
                    elif 128 < pygame.mouse.get_pos()[1] < 233:
                        if pos[6] != ' ':
                            continue
                        else:
                            pos[6] = jog[0]
                            return
                    elif 248 < pygame.mouse.get_pos()[1] < 360:
                        if pos[3] != ' ':
                            continue
                        else:
                            pos[3] = jog[0]
                            return


def copiatab(tabu):
    copia = []
    for l in tabu:
        copia.append(l)
    return copia


def computador(cpu):
    do = False
    while not do:
        for i in range(1, 10):
            cop = copiatab(pos)
            if pos[i] == ' ':
                cop[i] = cpu[1]
                if venceu(cop, pecas(cont), 'c'):
                    pos[i] = cpu[1]
                    return
        for i in range(1, 10):
            cop = copiatab(pos)
            if pos[i] == ' ':
                cop[i] = cpu[0]
                if venceu(cop, pecas(cont), 'p'):
                    pos[i] = cpu[1]
                    return
        if pos[7] == ' ' or pos[9] == ' ' or pos[1] == ' ' or pos[3] == ' ':
            a = [7, 9, 1, 3]
            b = choice(a)
            if not pos[b] != ' ':
                pos[b] = cpu[1]
                do = True
        elif pos[5] == ' ':
            pos[5] = cpu[1]
            do = True
        else:
            a = [8, 4, 6, 2]
            b = choice(a)
            if not pos[b] != ' ':
                pos[b] = cpu[1]
                do = True


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
    for j in range(1, 10):
        if pos[j] == ' ':
            return True


def pyg():
    for i in range(1, 10):
        if pos[i] != ' ':
            if pos[i] == 'X':
                if i == 1:
                    screen.blit(x, (-20, 225))
                elif i == 2:
                    screen.blit(x, (105, 225))
                elif i == 3:
                    screen.blit(x, (230, 225))
                elif i == 4:
                    screen.blit(x, (-20, 110))
                elif i == 5:
                    screen.blit(x, (105, 110))
                elif i == 6:
                    screen.blit(x, (230, 110))
                elif i == 7:
                    screen.blit(x, (-20, -15))
                elif i == 8:
                    screen.blit(x, (105, -15))
                elif i == 9:
                    screen.blit(x, (230, -15))
            elif pos[i] == 'O':
                if i == 1:
                    screen.blit(o, (-20, 225))
                elif i == 2:
                    screen.blit(o, (105, 225))
                elif i == 3:
                    screen.blit(o, (230, 225))
                elif i == 4:
                    screen.blit(o, (-20, 105))
                elif i == 5:
                    screen.blit(o, (105, 105))
                elif i == 6:
                    screen.blit(o, (230, 105))
                elif i == 7:
                    screen.blit(o, (-20, -15))
                elif i == 8:
                    screen.blit(o, (105, -15))
                elif i == 9:
                    screen.blit(o, (230, -15))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()


def clear(bo, pec, tur):
    pyg()
    if venceu(bo, pec, tur):
        if tur == 'p':
            le = pec[0]
        else:
            le = pec[1]
        if bo[7] == le and bo[8] == le and bo[9] == le:
            if le == 'X':
                screen.blit(X, (-20, -15))
                screen.blit(X, (105, -15))
                screen.blit(X, (230, -15))
            else:
                screen.blit(O, (-20, -15))
                screen.blit(O, (105, -15))
                screen.blit(O, (230, -15))
            pygame.draw.line(screen, (0, 0, 255), [30, 60], [330, 60], 10)
        elif bo[4] == le and bo[5] == le and bo[6] == le:
            if le == 'X':
                screen.blit(X, (-20, 110))
                screen.blit(X, (105, 110))
                screen.blit(X, (230, 110))
            else:
                screen.blit(O, (-20, 105))
                screen.blit(O, (105, 105))
                screen.blit(O, (230, 105))
            pygame.draw.line(screen, (0, 0, 255), [30, 180], [330, 180], 10)
        elif bo[1] == le and bo[2] == le and bo[3] == le:
            if le == 'X':
                screen.blit(X, (-20, 225))
                screen.blit(X, (105, 225))
                screen.blit(X, (230, 225))
            else:
                screen.blit(O, (-20, 225))
                screen.blit(O, (105, 225))
                screen.blit(O, (230, 225))
            pygame.draw.line(screen, (0, 0, 255), [30, 300], [330, 300], 10)
        elif bo[7] == le and bo[4] == le and bo[1] == le:
            if le == 'X':
                screen.blit(X, (-20, -15))
                screen.blit(X, (-20, 110))
                screen.blit(X, (-20, 225))
            else:
                screen.blit(O, (-20, -15))
                screen.blit(O, (-20, 105))
                screen.blit(O, (-20, 225))
            pygame.draw.line(screen, (0, 0, 255), [55, 30], [55, 330], 10)
        elif bo[8] == le and bo[5] == le and bo[2] == le:
            if le == 'X':
                screen.blit(X, (105, -15))
                screen.blit(X, (105, 110))
                screen.blit(X, (105, 225))
            else:
                screen.blit(O, (105, -15))
                screen.blit(O, (105, 105))
                screen.blit(O, (105, 225))
            pygame.draw.line(screen, (0, 0, 255), [180, 30], [180, 330], 10)
        elif bo[9] == le and bo[6] == le and bo[3] == le:
            if le == 'X':
                screen.blit(X, (230, -15))
                screen.blit(X, (230, 110))
                screen.blit(X, (230, 225))
            else:
                screen.blit(O, (230, -15))
                screen.blit(O, (230, 105))
                screen.blit(O, (230, 225))
            pygame.draw.line(screen, (0, 0, 255), [300, 30], [300, 330], 10)
        elif bo[7] == le and bo[5] == le and bo[3] == le:
            if le == 'X':
                screen.blit(X, (-20, -15))
                screen.blit(X, (105, 110))
                screen.blit(X, (230, 225))
            else:
                screen.blit(O, (-20, -15))
                screen.blit(O, (105, 105))
                screen.blit(O, (230, 225))
            pygame.draw.line(screen, (0, 0, 255), [20, 20], [340, 340], 10)
        elif bo[9] == le and bo[5] == le and bo[1] == le:
            if le == 'X':
                screen.blit(X, (230, -15))
                screen.blit(X, (105, 110))
                screen.blit(X, (-20, 225))
            else:
                screen.blit(O, (230, -15))
                screen.blit(O, (105, 105))
                screen.blit(O, (-20, 225))
            pygame.draw.line(screen, (0, 0, 255), [20, 340], [340, 20], 10)
        if tur == 'p':
            pygame.draw.rect(screen, (0, 255, 0), [100, 140, 180, 60])
            text = font.render(' Você venceu!', True, (0, 0, 0))
            screen.blit(text, (100, 160))
        else:
            pygame.draw.rect(screen, (255, 0, 0), [60, 140, 260, 60])
            text = font.render(' Computador venceu!', True, (0, 0, 0))
            screen.blit(text, (60, 160))
    else:
        pygame.draw.rect(screen, (255, 255, 0), [80, 140, 240, 60])
        text = font.render('  O jogo deu velha!', True, (0, 0, 0))
        screen.blit(text, (80, 160))
    pygame.display.flip()
    click = False
    while not click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if pygame.mouse.get_pressed(num_buttons=3) == (1, 0, 0):
                click = True
    screen.fill(white)
    screen.blit(board, (0, 0))
    sleep(1)


done = False
while cont < 5:
    cont += 1
    pos = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    if cont % 2:
        while True:
            pyg()
            player(pecas(cont))
            turno = 'p'
            if venceu(pos, pecas(cont), turno):
                pl += 1
                clear(pos, pecas(cont), turno)
                break
            elif not empate():
                em += 1
                clear(pos, pecas(cont), turno)
                break
            pyg()
            sleep(1)
            computador(pecas(cont))
            turno = 'c'
            if venceu(pos, pecas(cont), turno):
                pc += 1
                clear(pos, pecas(cont), turno)
                break
            elif not empate():
                em += 1
                clear(pos, pecas(cont), turno)
                break
    else:
        while True:
            pyg()
            sleep(1)
            computador(pecas(cont))
            turno = 'c'
            if venceu(pos, pecas(cont), turno):
                pc += 1
                clear(pos, pecas(cont), turno)
                break
            elif not empate():
                em += 1
                clear(pos, pecas(cont), turno)
                break
            pyg()
            player(pecas(cont))
            turno = 'p'
            if venceu(pos, pecas(cont), turno):
                pl += 1
                clear(pos, pecas(cont), turno)
                break
            elif not empate():
                em += 1
                clear(pos, pecas(cont), turno)
                break

while True:
    screen.fill(white)
    finalLines = ['O jogo terminou', f'Venceu {pl} vezes', f'Perdeu {pc} vezes', f'Houve {em} empates']
    y = 100
    for line in finalLines:
        win = pygame.font.SysFont('None', 48).render(line, True, (0, 0, 0))
        screen.blit(win, (50, y))
        y += 30
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()