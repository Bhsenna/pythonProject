# Programa de casa de câmbio. Crie um programa que pergunte qual moeda deseja
# obter, e qual moeda irá dar em troca
# Moedas a considerar: Dólar, Real, Euro e Libra esterlina
# informar as cotações das moedas em uma variável, já no início do código

sym = ['$', 'R$', '€', '£']
quer = int(input('Quero:\n(1) Dólar\n(2) Real\n(3) Euro\n(4) Libra esterlina\n'))
tem = int(input('Tenho:\n(1) Dólar\n(2) Real\n(3) Euro\n(4) Libra esterlina\n'))

if tem == 1:
  s2 = sym[tem-1]
  if quer == 1:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2+str(val)}')
  elif quer == 2:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2}{(val / 5.0819):.2f}')
  elif quer == 3:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2}{(val / 0.948):.2f}')
  elif quer == 4:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2}{(val / 0.8104056):.2f}')
  else:
    print('Moeda indisponível')
elif tem == 2:
  s2 = sym[tem-1]
  if quer == 1:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2}{(val / 0.19677679):.2f}')
  elif quer == 2:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2+str(val)}')
  elif quer == 3:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2}{(val / 0.1865443969):.2f}')
  elif quer == 4:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2}{(val / 0.1594690125):.2f}')
  else:
    print('Moeda indisponível')
elif tem == 3:
  s2 = sym[tem-1]
  if quer == 1:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2}{(val / 1.054):.2f}')
  elif quer == 2:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2}{(val / 5.3563226):.2f}')
  elif quer == 3:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2+str(val)}')
  elif quer == 4:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2}{(val / 0.8541675024):.2f}')
  else:
    print('Moeda indisponível')
elif tem == 4:
  s2 = sym[tem-1]
  if quer == 1:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2}{(val / 1.23395):.2f}')
  elif quer == 2:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2}{(val / 6.270810505):.2f}')
  elif quer == 3:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2}{(val / 1.1697846):.2f}')
  elif quer == 4:
    s1 = sym[quer-1]
    val = int(input(f'Valor Desejado: {s1}'))
    print(f'Valor Necessário: {s2+str(val)}')
  else:
    print('Moeda indisponível')
else:
  print('Moeda indisponível')