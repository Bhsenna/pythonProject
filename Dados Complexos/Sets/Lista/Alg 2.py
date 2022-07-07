cA = open('Candidato A.txt')
cB = open('Candidato B.txt')
cA = cA.read().splitlines()
cB = cB.read().splitlines()

print(f'Candidato A: {len(cA)} votos')
print(f'Candidato B: {len(cB)} votos')

if len(cA) > len(cB):
    print('Candidato A venceu a eleição')
elif len(cA) < len(cB):
    print('Candidato B venceu a eleição')
else:
    print('A eleição foi um Empate!')

tot = cA + cB
set1 = set()

for i in tot:
    if i in cA and i in cB:
        set1.add(i)
        for j in range(cA.count(i) - 1):
            cA.remove(i)
        for j in range(cB.count(i) - 1):
            cB.remove(i)

setA = set(cA)
setB = set(cB)

print(f'\nVotaram em ambos: {len(set1)}')
print(f'Não votaram: {100 - (len(setA.union(setB)))}\n')

print(f'Candidato A: {len(setA)} votos')
print(f'Candidato B: {len(setB)} votos')

if len(setA) > len(setB):
    print('Candidato A venceu a eleição')
elif len(setA) < len(setB):
    print('Candidato B venceu a eleição')
else:
    print('A eleição foi um Empate!')