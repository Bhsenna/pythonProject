print('\x1b[38;5;3mDUPLAS!\n')

mu = []
for i in range(3):
    mu.append(input(f'Mulher {i+1}: '))
print(f'\nMulheres: {mu}\n')

ho = []
for j in range(3):
    ho.append(input(f'Homem {j+1}: '))
print(f'\nHomens: {ho}\n')

for k in range(3):
    print(f'Dupla {k+1}: {mu[k]} e {ho[k]}')