import pygame

pygame.init()
white = (255, 255, 255)
screen = pygame.display.set_mode((360, 360))

pygame.display.set_caption('Tic Tac Toe')

board = pygame.image.load(r'D:\Programação\ActualEntra21\Desafios\1Pzpe.png')
x = pygame.image.load(r'D:\Programação\ActualEntra21\Desafios\tic-tac-toe_39453.png')
o = pygame.image.load(r'D:\Programação\ActualEntra21\Desafios\tic-tac-toe_39453 (1).png')

while True:
    screen.fill(white)
    screen.blit(board, (0, 0))
    screen.blit(x, (-20, -15))
    screen.blit(x, (105, 110))
    screen.blit(o, (230, 225))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()