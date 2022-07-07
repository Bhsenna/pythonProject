from random import choice
from time import sleep
import pygame

pygame.init()
canto = (0, 255, 64)
sq1 = (150, 255, 150)
sq2 = (200, 255, 200)
screen = pygame.display.set_mode((360, 330))
pygame.display.set_caption('Snake - Por: Hazime')
clock = pygame.time.Clock()
snakehead = pygame.image.load(r'Head.png')
snakebody = pygame.image.load(r'Body.png')
apl = pygame.image.load('Apple_30x30.png')
font = pygame.font.SysFont('None', 36)


def board():
    screen.fill(canto)
    x, y = 30, 30
    j, k = 1, 1
    for l in range(90):
        if k % 2:
            pygame.draw.rect(screen, sq1, (x, y, 30, 30))
            if j % 10:
                k = 0
        else:
            pygame.draw.rect(screen, sq2, (x, y, 30, 30))
            if j % 10:
                k = 1
        if not j % 10 and j != 0:
            y += 30
            x = 30
        else:
            x += 30
        j += 1


def empty():
    emp = []
    for l in range(len(pos)):
        if pos[l] == ' ':
            emp.append(l)
    return emp


def apple():
    place = choice(empty())
    pos[place] = 'apple'


def snake():
    board()
    j = 0
    for i in body:
        X = 30 + (30 * (i % 10))
        if i <= 9:
            Y = 30
        elif i <= 19:
            Y = 30 * 2
        elif i <= 29:
            Y = 30 * 3
        elif i <= 39:
            Y = 30 * 4
        elif i <= 49:
            Y = 30 * 5
        elif i <= 59:
            Y = 30 * 6
        elif i <= 69:
            Y = 30 * 7
        elif i <= 79:
            Y = 30 * 8
        else:
            Y = 30 * 9
        pygame.draw.rect(screen, bod[j], (X, Y, 30, 30))
        j += 1
    for i in range(len(pos)):
        X = 30 + (30 * (i % 10))
        if i <= 9:
            Y = 30
        elif i <= 19:
            Y = 30 * 2
        elif i <= 29:
            Y = 30 * 3
        elif i <= 39:
            Y = 30 * 4
        elif i <= 49:
            Y = 30 * 5
        elif i <= 59:
            Y = 30 * 6
        elif i <= 69:
            Y = 30 * 7
        elif i <= 79:
            Y = 30 * 8
        else:
            Y = 30 * 9
        if pos[i] == 'head':
            if dire == 'left':
                new_snakehead = pygame.transform.rotate(snakehead, 90)
                screen.blit(new_snakehead, (X, Y))
            elif dire == 'right':
                new_snakehead = pygame.transform.rotate(snakehead, -90)
                screen.blit(new_snakehead, (X, Y))
            elif dire == 'up':
                new_snakehead = pygame.transform.rotate(snakehead, 0)
                screen.blit(new_snakehead, (X, Y))
            elif dire == 'down':
                new_snakehead = pygame.transform.rotate(snakehead, 180)
                screen.blit(new_snakehead, (X, Y))
            else:
                new_snakehead = pygame.transform.rotate(snakehead, -90)
                screen.blit(new_snakehead, (X, Y))
        elif pos[i] == 'apple':
            screen.blit(apl, (X, Y))
    if not empty():
        pygame.draw.rect(screen, (0, 255, 0), [60, 140, 260, 60])
        text = font.render('       Você venceu!', True, (0, 0, 0))
        screen.blit(text, (60, 160))
        pygame.display.update()
        click = False
        while not click:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if pygame.key.get_focused():
                    click = True
                    sleep(0.2)
        return 'break'
    if 'apple' not in pos:
        length.append('body')
        a = 175 - (len(length) * 2)
        bod.insert(0, (0, a, 255))
        apple()
    pygame.display.update()


def move(mov):
    a = pos.index('head')
    if mov == 'left':
        if not a % 10 or pos[a - 1] not in (' ', 'apple'):
            pygame.draw.rect(screen, (255, 0, 0), [60, 140, 260, 60])
            text = font.render('        Você bateu!', True, (0, 0, 0))
            screen.blit(text, (60, 160))
            pygame.display.update()
            click = False
            while not click:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif pygame.key.get_focused():
                        click = True
                        sleep(0.2)
            return 'break'
        else:
            pos[a], pos[a - 1] = 'body', 'head'
            body.append(a)
            if len(body) > len(length):
                pos[body.pop(0)] = ' '
    if mov == 'right':
        if a in (9, 19, 29, 39, 49, 59, 69, 79, 89) or pos[a + 1] not in (' ', 'apple'):
            pygame.draw.rect(screen, (255, 0, 0), [60, 140, 260, 60])
            text = font.render('        Você bateu!', True, (0, 0, 0))
            screen.blit(text, (60, 160))
            pygame.display.update()
            click = False
            while not click:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif pygame.key.get_focused():
                        click = True
                        sleep(0.2)
            return 'break'
        else:
            pos[a], pos[a + 1] = 'body', 'head'
            body.append(a)
            if len(body) > len(length):
                pos[body.pop(0)] = ' '
    if mov == 'down':
        if a + 10 > 89 or pos[a + 10] not in (' ', 'apple'):
            pygame.draw.rect(screen, (255, 0, 0), [60, 140, 260, 60])
            text = font.render('        Você bateu!', True, (0, 0, 0))
            screen.blit(text, (60, 160))
            pygame.display.update()
            click = False
            while not click:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif pygame.key.get_focused():
                        click = True
                        sleep(0.2)
            return 'break'
        else:
            pos[a], pos[a + 10] = 'body', 'head'
            body.append(a)
            if len(body) > len(length):
                pos[body.pop(0)] = ' '
    if mov == 'up':
        if a - 10 < 0 or pos[a - 10] not in (' ', 'apple'):
            pygame.draw.rect(screen, (255, 0, 0), [60, 140, 260, 60])
            text = font.render('        Você bateu!', True, (0, 0, 0))
            screen.blit(text, (60, 160))
            pygame.display.update()
            click = False
            while not click:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif pygame.key.get_focused():
                        click = True
                        sleep(0.2)
            return 'break'
        else:
            pos[a], pos[a - 10] = 'body', 'head'
            body.append(a)
            if len(body) > len(length):
                pos[body.pop(0)] = ' '


while True:
    pos = []
    for p in range(90):
        pos.append(' ')
    board()
    pos[47] = 'apple'
    pos[42] = 'head'
    length = ['body', 'body']
    bod = [(0, 171, 255), (0, 173, 255)]
    body = []
    dire = None
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
        if pygame.key.get_pressed()[pygame.K_LEFT] and dire != 'right':
            dire = 'left'
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and dire != 'left':
            dire = 'right'
        elif pygame.key.get_pressed()[pygame.K_UP] and dire != 'down':
            dire = 'up'
        elif pygame.key.get_pressed()[pygame.K_DOWN] and dire != 'up':
            dire = 'down'
        if move(dire) == 'break':
            break
        if snake() == 'break':
            break
        clock.tick(8)