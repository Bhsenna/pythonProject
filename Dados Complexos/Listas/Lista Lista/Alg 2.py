nomes, inp = [], ' '
while inp != '':
    inp = input('Informe os nomes (Enter vazio para parar): ')
    nomes.append(inp)
nomes.pop()

for i in range(len(nomes)):
    nomes[i] = nomes[i].lower().title().strip()

nomes.sort()
print(f'Crescente: {nomes}')
nomes.sort(reverse=True)
print(f'Decrescente: {nomes}')
print(f'Quantidade de nomes: {len(nomes)}')
print(f'Carlos: {nomes.count("Carlos")}')