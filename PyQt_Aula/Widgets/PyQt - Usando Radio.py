from PyQt5 import uic, QtWidgets


def funcao_principal():
    if janela.radioButton.isChecked():
        opcao = 'Vermelho'
    elif janela.radioButton_2.isChecked():
        opcao = 'Verde'
    elif janela.radioButton_3.isChecked():
        opcao = 'Azul'
    elif janela.radioButton_4.isChecked():
        opcao = 'Amarelo'
    else:
        opcao = ''

    janela.label_2.setText(f'Cor Escolhida: {opcao}')


app = QtWidgets.QApplication([])
janela = uic.loadUi("Janela-Radio.ui")
janela.pushButton.clicked.connect(funcao_principal)

janela.show()
app.exec()