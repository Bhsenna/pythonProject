nota = 7.8
freq = 0.7  # 0.6 equivale a 60%

if nota >= 7 and freq >= 0.75:  # ambos devem ser verdade
    print('Parabéns, você passou de ano!')
else:
    print('Ah não, você reprovou...')

if nota >= 7 or freq >= 0.75:  # apenas 1 precisa ser verdade
    print('Parabéns, você passou de ano!')
else:
    print('Ah não, você reprovou...')