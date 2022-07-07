from random import randint as ri
from operator import itemgetter as ig


def pegar():
    nome = input('Nome do Jogador:\n').strip().capitalize()
    dado = ri(1, 6)
    dic[nome] = dado


dic = {}
for i in range(5):
    pegar()

ordem = sorted(dic.items(), key=ig(1), reverse=True)
for i, res in enumerate(ordem):
    print(f'{i+1} - {res[0]} - {res[1]}')