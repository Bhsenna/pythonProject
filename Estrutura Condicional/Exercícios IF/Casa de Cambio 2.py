moedas = [4.8116, 1, 5.1655, 6.0328448]
sym = ['$', 'R$', '€', '£']
print(50*'=')
print("CASA DE CÂMBIO".center(50))
print(50*'=')

while True:
    quer = input('QUERO:\n(1) Dólar\n(2) Real\n(3) Euro\n(4) Libra esterlina\n')
    if quer.strip() not in "1234":
        print('Moeda indisponível\n')
    else:
        quer = int(quer)
        break
while True:
    tem = input('TENHO:\n(1) Dólar\n(2) Real\n(3) Euro\n(4) Libra esterlina\n')
    if tem.strip() not in "1234":
        print('Moeda indisponível\n')
    else:
        tem = int(tem)
        break

valDes = float(input(f'Valor Desejado: {sym[quer-1]}'))

print(f'Você precisa de {sym[quer-1]}{(valDes * moedas[quer-1] / moedas[tem-1]):.2f}')