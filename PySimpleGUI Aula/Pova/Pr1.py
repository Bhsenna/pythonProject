import PySimpleGUI as sg

layout = [
    [sg.Text('ALUNO', size=30, font=30, justification='c')],
    [sg.Frame('', [
        [sg.Text('Nome:', size=10), sg.Input(size=24)],
        [sg.Text('Idade:', size=10), sg.Input(size=24)],
        [sg.Button('OK'), sg.Text('Temas:'), sg.Combo(sg.theme_list(), key='tema')]
    ])]
]
janela = sg.Window('Exercício', layout)
while True:
    eventos, valores = janela.read()
    if eventos == 'OK':
        sg.theme(valores['tema'])
        janela.close()
        layout = [
            [sg.Text('ALUNO', size=30, font=30, justification='c')],
            [sg.Frame('', [
                [sg.Text('Nome:', size=10), sg.Input(size=24)],
                [sg.Text('Idade:', size=10), sg.Input(size=24)],
                [sg.Button('OK'), sg.Text('Temas:'), sg.Combo(sg.theme_list(), key='tema')]
            ])]
        ]
        janela = sg.Window('Aula', layout)
        eventos, valores = janela.read()
    elif eventos == sg.WINDOW_CLOSED:
        break