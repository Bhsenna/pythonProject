print('\x1b[38;5;3mCADASTRO DE PRODUTOS!\n')

num = input('Quantos produtos você deseja cadastrar?\nResposta: ')
while type(num) != int:
    try:
        num = int(num)
    except:
        print('Número inválido, tente novamente')
        num = input('\nQuantos produtos você deseja cadastrar?\nResposta: ')

print('\n' + 40 * '=' + '\n')
prod = []
pre = []
for i in range(num):
    prod.append(input(f'Produto {i+1}: ').strip())
    pre.append(input(f'Preço: R$ ').strip().replace(',', '.'))
    print()

print(40 * '=' + '\n')

for j in range(num):
    print(f'Produto: {prod[j]} - Preço: R$ {pre[j]}')