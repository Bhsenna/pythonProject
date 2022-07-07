import PySimpleGUI as sg

layout = [
    [sg.Text('Time 1'), sg.Input(key='tim1', size=(10, 1)), sg.Spin(list(range(1, 100)), key='pon1', enable_events=True)],
    [sg.Text('Time 2'), sg.Input(key='tim2', size=(10, 1)), sg.Spin(list(range(1, 100)), key='pon2', enable_events=True)],
    [sg.Text('Time 3'), sg.Input(key='tim3', size=(10, 1)), sg.Spin(list(range(1, 100)), key='pon3', enable_events=True)],
    [sg.Text('Time vencedor:   ', key='winner')]
]
janela = sg.Window('Aual', layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    dic = {valores['tim1']: valores['pon1'], valores['tim2']: valores['pon2'], valores['tim3']: valores['pon3']}
    win = max(dic, key=dic.get)
    count = 0
    for i in dic:
        if dic[i] == dic[win]:
            count += 1
    if count > 1:
        janela['winner'].Update('Time vencedor:   Empate')
    else:
        janela['winner'].Update(f'Time vencedor:   {win}')