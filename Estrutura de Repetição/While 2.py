continuar = 's'
contador = 1

while continuar.lower() == 's':
    print(contador)
    contador += 1
    continuar = input('Desejas continuar? (S ou n): ')
print('Adios Muchacho')