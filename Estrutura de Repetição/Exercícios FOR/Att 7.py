import random

# num = input('Quantos times há na série A?\nResposta: ')
# while type(num) != int:
#     try:
#         num = int(num)
#     except:
#         print('Número inválido, tente novamente')
#         num = input('\nQuantos times há na série A?\nResposta: ')
#
# times = input(f'{num} times - ').split(', ')
# while len(times) < num:
#     faltam = input(f'Ainda faltam {num - len(times)} times!\n- ').split(', ')
#     times = times + faltam
# if len(times) > num:
#     print('Times demais, tente novamente')
#     exit()
times = open("times.txt", "r")
times = times.read().splitlines()
times2 = times

pontos = []
saldo = []
for j in range(len(times)):
    pontos.append(0)
    saldo.append(0)

for i in range(len(times)):
    for n in range(len(times2)):
        if i == n:
            continue
        else:
            jog1, jog2 = random.randint(0, 3), random.randint(0, 3)
            if jog1 > jog2:
                pontos[i] += 3
            elif jog1 < jog2:
                pontos[n] += 3
            elif jog1 == jog2:
                pontos[i] += 1
                pontos[n] += 1
            saldo[i] += jog1
            saldo[n] += jog2
            print(f'{times[i]} [{jog1}] x [{jog2}] {times2[n]}')
print()

ranking = []
for k in range(len(times)):
    ranking.append(f'{pontos[k]} - \33[1;32;1m{times[k]}\33[1;0m')
    #print(f'{times[k]} - {pontos[k]} pontos / {saldo[k]} gols')

ranking.sort(reverse=True)
for m in range(len(ranking)):
    if m < 4:
        print(f'\33[1;44m \33[1;0m \33[1;34;1m{ranking[m]}')
    elif m < 6:
        print(f'\33[1;45m \33[1;0m \33[1;35;1m{ranking[m]}')
    elif m < 12:
        print(f'\33[1;42m \33[1;0m \33[1;32;1m{ranking[m]}')
    elif m > len(ranking) - 5:
        print(f'\33[1;41m \33[1;0m \33[1;31;1m{ranking[m]}')
    else:
        print(f'\33[1;0m  {ranking[m]}')
timeV = 0
for l in range(len(times)):
    if pontos[l] > pontos[timeV]:
        timeV = pontos.index(pontos[l])
    elif pontos[l] == timeV:
        if saldo[pontos.index(timeV)] > saldo[l]:
            timeV = saldo.index(saldo[pontos.index(timeV)])
print(f'{times[timeV]} foi o vencedor')