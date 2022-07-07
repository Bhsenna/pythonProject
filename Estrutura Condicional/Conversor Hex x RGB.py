# Forma autoral do balacobaco:
R, G, B = 300, 300, 300
Hex = '0 1 2 3 4 5 6 7 8 9 A B C D E F'.split()
while not (255 >= R >= 0 and 255 >= G >= 0 and 255 >= B >= 0):
    R = int(input('Digite R: '))
    G = int(input('Digite G: '))
    B = int(input('Digite B: '))
    if 255 >= R >= 0 and 255 >= G >= 0 and 255 >= B >= 0:
        hexR = f'{Hex[(R // 16)] + Hex[int(((R / 16) - (R // 16)) * 16)]}'
        hexG = f'{Hex[(G // 16)] + Hex[int(((G / 16) - (G // 16)) * 16)]}'
        hexB = f'{Hex[(B // 16)] + Hex[int(((B / 16) - (B // 16)) * 16)]}'
        print(f'#{hexR}{hexG}{hexB}')
    else:
        print('Números fora do Espectro RBG, tente novamente\n')

# Forma simples, com coisa das interwebs (não balacobaco):
R, G, B = 300, 300, 300
while not (255 >= R >= 0 and 255 >= G >= 0 and 255 >= B >= 0):
    R = int(input('Digite R: '))
    G = int(input('Digite G: '))
    B = int(input('Digite B: '))
    if 255 >= R >= 0 and 255 >= G >= 0 and 255 >= B >= 0:
        print('#%02X%02X%02X' % (R, G, B))
    else:
        print('Números fora do Espectro RBG, tente novamente\n')
