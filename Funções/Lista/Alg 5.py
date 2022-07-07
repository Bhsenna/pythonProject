import Func as f

J = [0, 0, 0]
b = 0
for i in range(3):
    a = f.rps()
    while a == b:
        print('Você já jogou Pedra na última, não vale repetir!')
        a = f.rps()
    f.rps_timer()
    c = f.rps_game(a, f.rps_pc())
    J[c] += 1
    print()
    if a == 'Pedra':
        b = a

print(f'FIM DE JOGO\nVitórias Jogador: {J[2]}\nVitórias Computador: {J[1]}\nEmpates: {J[0]}')