import PySimpleGUI as sg

layout = [
    [sg.Text('Avaliação da Aula', font=30, size=20, justification='c')],
    [sg.Text('O quanto você gostou da aula', size=24, justification='c')],
    [sg.Image(key='emo')],
    [sg.Slider((1.0, 10.0), orientation='h', size=(24, 20), key='Slider', enable_events=True)],
    [sg.Text('Observações:', size=24, justification='c')],
    [sg.Input(size=30)],
    [sg.Button('ENVIAR')]
]
janela = sg.Window('Avaliação', layout, element_justification='c')
while True:
    eventos, valores = janela.read()
    if eventos == 'Slider':
        if valores['Slider'] == 1:
            janela['emo'].Update(sg.EMOJI_BASE64_DEAD)
        elif valores['Slider'] == 2:
            janela['emo'].Update(sg.EMOJI_BASE64_DEAD)
        elif valores['Slider'] == 3:
            janela['emo'].Update(sg.EMOJI_BASE64_SAD)
        elif valores['Slider'] == 4:
            janela['emo'].Update(sg.EMOJI_BASE64_SAD)
        elif valores['Slider'] == 5:
            janela['emo'].Update(sg.EMOJI_BASE64_SAD)
        elif valores['Slider'] == 6:
            janela['emo'].Update(sg.EMOJI_BASE64_HAPPY_BIG_SMILE)
        elif valores['Slider'] == 7:
            janela['emo'].Update(sg.EMOJI_BASE64_HAPPY_BIG_SMILE)
        elif valores['Slider'] == 8:
            janela['emo'].Update(sg.EMOJI_BASE64_HAPPY_HEARTS)
        elif valores['Slider'] == 9:
            janela['emo'].Update(sg.EMOJI_BASE64_HAPPY_HEARTS)
        elif valores['Slider'] == 10:
            janela['emo'].Update(sg.EMOJI_BASE64_HAPPY_HEARTS)
    if eventos == (sg.WINDOW_CLOSED or 'ENVIAR'):
        break