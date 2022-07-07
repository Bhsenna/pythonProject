import PySimpleGUI as sg

# print(sg.theme_list())


# print('Olá, Mundo')


# sg.popup('Olá, Mundo')


# sg.popup_ok_cancel('Olá, Mundo')


# sg.popup_notify('Enviado!')


# Composição base de uma janela
# layout | janela | ler janela


# layout = [
#     [sg.Text('Olá, Mundo')]
# ]


# layout = [
#     [sg.Text('Olá, Mundo')],    # Atenção para a vírgula
#     [sg.Button('OK')]
# ]


# janela = sg.Window()


# janela = sg.Window('Titulo', layout)


# janela = sg.Window('Aula', layout)


# janela.read()


# Criar janela com seu nome e um botão


# layout = [
    # [sg.Text('Ola Mundo')],
    # [sg.Input()],
    # [sg.Multiline()],
    # [sg.Combo(['Paulo', 'Rodrigo'])],
    # [sg.Checkbox('Deficiente?')],
    # [sg.Radio('sim', 'opc'), sg.Radio('nao', 'opc'), sg.Radio('talvez', 'opc')],    # Se o 'opc' for diferente, multiplas opições poderão ser selecionadas
    # [sg.Spin(list(range(1, 100)))],
    # [sg.Slider((1, 100))],
    # [sg.Button('OK')],
    # [sg.Image(r'Apple_30x30.png')],
    # [sg.Frame('Janela Frame', [
    #     [sg.Text('Frase')],
    #     [sg.Button('OK')]
    # ])],
# ]
# janela = sg.Window('Aula', layout)
# janela.read()


# SALVAR VALORES E EVENTOS
# layout = [
#     [sg.Input(key='Nome')],
#     [sg.Button('Salvar')]
# ]
# janela = sg.Window('Aula', layout)
# eventos, valores = janela.read()
# print(eventos)
# print(valores)
# if eventos == 'Salvar':
#     print('Nome salvo')
#     print(valores['Nome'])


# WHILE TRUE
# layout = [
#     [sg.Input(key='Nome')],
#     [sg.Slider((1, 100))],
#     [sg.Button('Salvar')]
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     print(eventos)
#     print(valores)
#     if eventos == 'Salvar':
#         print('Nome salvo')
#         print(valores['Nome'])
#     elif eventos == sg.WINDOW_CLOSED:
#         break


# ATUALIZAR VALORES
# layout = [
#     [sg.Text('OLA MUNDO', key='txt')],
#     [sg.Input(key='nome')],
#     [sg.Button('Salvar', key='btn')]
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     print(eventos)
#     print(valores)
#     if eventos == 'btn':
#         janela['nome'].Update('PAULO')
#         janela['txt'].Update('PAULO')
#         janela['btn'].Update('PAULO')
#     elif eventos == sg.WINDOW_CLOSED:
#         break


# ATRIBUTOS
# layout = [
#     # [sg.Input(key='nome', default_text='Digite aqui', background_color='Cyan')],
#     # [sg.Button('Salvar', border_width=10)],
#     # [sg.Slider((1.0, 11.0), orientation='h', size=(30,20), key='Slider')],
#     [sg.Text('OLA MUNDO', size=(30, 1), font=30, justification='c')],
#     [sg.Slider((1, 100), enable_events=True, key='slider', orientation='h')],
#     [sg.Button('Salvar')]
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     print(eventos)
#     print(valores)
#     if eventos == 'Salvar':
#         janela['slider'].Update(range=(1, 10))
#     elif eventos == sg.WINDOW_CLOSED:
#         break


# FECHAR JANELA
# layout = [
#     [sg.Input(key='nome')],
#     [sg.Button('Salvar')]
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     print(eventos)
#     print(valores)
#     if eventos == 'Salvar':
#         janela.close()    # Janela não pode mais ser reaberta
#         break


# REABRIR JANELA
# txtBotao = 'Salvar'
# sg.theme()
# layout = [
#     [sg.Input(key='nome')],
#     [sg.Button(txtBotao)],
#     [sg.Combo(sg.theme_list(), key='comboLista')]
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     if eventos == 'Salvar':
#         sg.theme(valores['comboLista'])
#         txtBotao = 'ola'
#         janela.close()
#         layout = [
#             [sg.Input(key='nome')],
#             [sg.Button(txtBotao)],
#             [sg.Combo(sg.theme_list())]
#         ]
#         janela = sg.Window('Aula', layout)
#         eventos, valores = janela.read()
#         break