from Funções.Lista.Func import getInt as gI


def pegar(j):
    nome = input('\nNome do Jogador:\n').strip().capitalize()
    partidas = gI('Número de Partidas:\n')
    gol = 0
    for k in range(partidas):
        gol += gI(f'Gols feitos na {k+1}° partidas: ')
    aprov = gol / partidas * 100
    dic[j] = {'Nome': nome, 'N° de Partidas': partidas, 'Saldo de gols': gol, 'Aproveitamento': f'{aprov:.2f}%'}
    return gol


dic = {}
n = gI('Quantos jogadores você deseja registrar:\n')
gol_Total = 0
for i in range(n):
    gol_Total += pegar(i)

for i in range(n):
    print()
    for j in dic[i]:
        print(j, dic[i][j], sep=': ')
print('\nTotal de Gols:', gol_Total)