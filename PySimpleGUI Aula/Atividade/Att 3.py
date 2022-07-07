import PySimpleGUI as sg

layout = [
    [sg.Text('Mercadão Atacadista Blumenau', font=30, justification='c')],
    [sg.Text('Selecione o método de pagamento:')],
    [sg.Radio('Cartão', 'opc'), sg.Radio('Cheque', 'opc'), sg.Radio('Dinheiro', 'opc')],
    [sg.Text('Digite o valor do produto 1:', key='prod'), sg.Input(key='val')],
    [sg.Button('Adicionar valor'), sg.Button('Finalizar compra')],
    [sg.Text('Valor Total: R$0', key='tot')]
]
janela = sg.Window('Aual', layout)
tot = 0
a = 1
while True:
    eventos, valores = janela.read()
    if eventos == 'Fechar Janela':
        break
    elif eventos == 'Adicionar valor':
        tot += float(valores['val'])
        a += 1
        janela['val'].Update('')
        janela['prod'].Update(f'Digite o valor do produto {a}:')
        janela['tot'].Update(f'Valor Total: R${tot}')
    elif eventos == 'Finalizar compra':
        layout = [
            [sg.Text('Compra Finalizada', font=30, justification='c')],
            [sg.Text(f'Valor total da compra: R${tot}')],
            [sg.Button('Fechar Janela')]
        ]
        janela = sg.Window('Aual', layout)
    elif eventos == sg.WINDOW_CLOSED:
        break