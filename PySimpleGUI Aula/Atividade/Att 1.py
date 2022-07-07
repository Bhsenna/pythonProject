import PySimpleGUI as sg

layout = [
    [sg.Text('Digite seu nome:'), sg.Input(key='nome')],
    [sg.Text('Digite seu Turma:'), sg.Input(key='turma')],
    [sg.Text('Matemática:'), sg.Spin(list(range(1, 11)), key='n1')],
    [sg.Text('Leitura:'), sg.Spin(list(range(1, 11)), key='n2')],
    [sg.Text('Música:'), sg.Spin(list(range(1, 11)), key='n3')],
    [sg.Text('Ciências:'), sg.Spin(list(range(1, 11)), key='n4')],
    [sg.Button('Calcular')],
    [sg.Text(f"Média:", key='med')]
]
while True:
    janela = sg.Window('Aula', layout)
    eventos, valores = janela.read()
    if eventos == 'Calcular':
        print(valores)
        media = (janela['n1'].get() + janela['n2'].get() + janela['n3'].get() + janela['n4'].get()) / 4
        janela['med'].Update(f"Média: {media}")
        if media >= 7:
            layout = [
                [sg.Text('Digite seu nome:'), sg.Input(key='nome', default_text=f"{valores['nome']}")],
                [sg.Text('Digite seu Turma:'), sg.Input(key='turma', default_text=f"{valores['turma']}")],
                [sg.Text('Matemática:'), sg.Spin(list(range(1, 11)), key='n1')],
                [sg.Text('Leitura:'), sg.Spin(list(range(1, 11)), key='n2')],
                [sg.Text('Música:'), sg.Spin(list(range(1, 11)), key='n3')],
                [sg.Text('Ciências:'), sg.Spin(list(range(1, 11)), key='n4')],
                [sg.Button('Calcular')],
                [sg.Text(f"Média: {media}", key='med')],
                [sg.Text('Aprovado')]
            ]
        else:
            layout = [
                [sg.Text('Digite seu nome:'), sg.Input(key='nome', default_text=f"{valores['nome']}")],
                [sg.Text('Digite seu Turma:'), sg.Input(key='turma', default_text=f"{valores['turma']}")],
                [sg.Text('Matemática:'), sg.Spin(list(range(1, 11)), key='n1')],
                [sg.Text('Leitura:'), sg.Spin(list(range(1, 11)), key='n2')],
                [sg.Text('Música:'), sg.Spin(list(range(1, 11)), key='n3')],
                [sg.Text('Ciências:'), sg.Spin(list(range(1, 11)), key='n4')],
                [sg.Button('Calcular')],
                [sg.Text(f"Média: {media}", key='med')],
                [sg.Text('Reprovado')]
            ]
    elif eventos == sg.WINDOW_CLOSED:
        break