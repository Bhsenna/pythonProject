"""
INFORME A QUANTIDADE DE LADOS, E AO FINAL, DIGA QUAL É A FIGURA GEOMÉTRICA
1 LADO, É PONTO
2 LADOS ... LINHA
3 LADOS ... TRIÂNGULO
4 LADOS ... RETÂNGULO
5 LADOS ... PENTAGONO
6 LADOS ... HEXAGONO

SE O NÚMERO FOR MAIOR QUE 6, TRAZER COMO RESPOSTA: VOCÊ ESTÁ CERTO DISSO?
"""

fig = int(input('Informe a quantidade de lados da sua figura: '))

if fig == 1:
    print('Sua figura é um: PONTO')
elif fig == 2:
    print('Sua figura é uma: LINHA')
elif fig == 3:
    print('Sua figura é um: TRIÂNGULO')
elif fig == 4:
    print('Sua figura é um: RETÂNGULO')
elif fig == 5:
    print('Sua figura é um: PENTAGONO')
elif fig == 6:
    print('Sua figura é um: HEXAGONO')
else:
    print('VOCÊ ESTÁ CERTO DISSO?')
