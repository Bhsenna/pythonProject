ant = open('clientes sistema antigo.txt')
ant = ant.read().splitlines()
nov = open('clientes sistema novo.txt')
nov = nov.read().splitlines()

total = len(ant) + len(nov)
print(f'Total de Cadastros: {total}')

tot = ant + nov
set3 = set()
for i in tot:
    if tot.count(i) > 1:
        set3.add(i)

set1 = set(ant)
set2 = set(nov)

print(f'Total de Duplicados: {len(set3)}')
print(f'Repetidos: {total - len(set2.union(set1))}')
print(f'Cadastros Únicos: {len(set2.union(set1))}')