rep = 's'
while rep == 's':
    mai = input('Informe a Massa Inicial (em gramas): ')
    if mai.lstrip('-').isdigit():
        mai = int(mai)

    time, num = 0, mai
    while num > 0.5:
        num = num / 2
        time += 50
    if time % 3600 == 0:
        time = f'{time // 3600} hora(s)'
    elif time % 60 == 0:
        time = f'{time // 60} minuto(s)'
    elif time > 3600:
        time = f'{time // 3600} horas, {(time - (3600 *(time // 3600))) // 60} minutos e {time % 60} segundos'
    elif time > 60:
        time = f'{time // 60} minutos e {time % 60} segundos'

    print(f'Para que o material vá de {mai} gramas para {num} gramas, será necessário esperar {time}')

    rep = input('Quer testar com outra massa? (S ou N)\n').lower()