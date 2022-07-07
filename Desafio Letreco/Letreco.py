# \33[42m - Green
# \33[43m - Yellow
# \33[41m - Red
# \33[0m  - Reset
import random

print('\33[1;33m L \33[1;31mE \33[1;0mT R \33[1;32;1mE \33[1;0mC O\33[0m')
win = False
opc = open("dicionario 5 letras sem acentos.txt", encoding="utf-8", mode="r")
opc2 = open("dicionario palavras.txt", encoding="utf-8", mode="r")
opc = opc.read().splitlines()
opc2 = opc2.read().splitlines()
cho = random.randint(0, len(opc))
pa = list(opc[cho].upper())
pa2 = list(opc2[cho].upper())
tent, i = 0, 0

alp = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
alp2 = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
letUs = []

while i <= 6:
    check = list('check')
    cont = 0
    tent += 1
    print(f'\nVocê tem {7 - i} tentativas restantes')
    i += 1
    rep = list(input('Digite uma palavra de 5 letras: ').upper().strip())
    if ''.join(rep).lower() not in opc:
        print('Palavra não reconhecida, tente novamente')
        i -= 1
        tent -= 1
    elif len(rep) == 5:
        if rep == pa:
            win = True
        for j in range(len(pa)):
            if rep[j] == pa[j]:
                alp[alp2.index(rep[j])] = f'\33[0m\33[42;30m {rep[j]} \33[0m'
                letUs.append(rep[j])
                check[j] = f'\33[42;30m {pa2[j]}'
            elif rep[j] in pa and cont == 0:
                if any(rep.count(rep[j]) > 1 for element in rep) and not any(pa.count(rep[j]) > 1 for element in pa):
                    if pa[pa.index(rep[j])] == rep[pa.index(rep[j])]:
                        check[j] = f'\33[41;30m {rep[j]}'
                    else:
                        check[j] = f'\33[43;30m {rep[j]}'
                        if rep[j] not in letUs:
                            alp[alp.index(rep[j])] = f'\33[0m\33[43;30m {rep[j]} \33[0m'
                            letUs.append(rep[j])
                        cont += 1
                elif any(rep.count(rep[j]) > 1 for element in rep) and any(pa.count(rep[j]) > 1 for element in pa):
                    check[j] = f'\33[43;30m {rep[j]}'
                    if rep[j] not in letUs:
                        alp[alp.index(rep[j])] = f'\33[0m\33[43;30m {rep[j]} \33[0m'
                        letUs.append(rep[j])
                else:
                    check[j] = f'\33[43;30m {rep[j]}'
                    if rep[j] not in letUs:
                        alp[alp.index(rep[j])] = f'\33[0m\33[43;30m {rep[j]} \33[0m'
                        letUs.append(rep[j])
            else:
                if rep[j] not in letUs:
                    alp[alp.index(rep[j])] = f'\33[0m\33[41;30m {rep[j]} \33[0m'
                    letUs.append(rep[j])
                check[j] = f'\33[41;30m {rep[j]}'
        for k in range(len(check)):
            print(f'{check[k]} ', end='')
        print('\33[0m')
        if win:
            break
        print(f'\n{" ".join(alp)}\33[0m')

if win:
    print(f'PARABÉNS, VOCÊ GANHOU EM {tent} TENTATIVAS!')
else:
    print(f'Você perdeu, e a palavra era {"".join(pa)}')