from PyQt5 import uic, QtWidgets


def salvar():
    nome = tela.lineEdit.text()
    idade = tela.lineEdit_2.text()
    tel = tela.lineEdit_3.text()
    dados = f"Nome: {nome}\nIdade: {idade}\nTelefone: {tel}"

    arquivo = QtWidgets.QFileDialog.getSaveFileName()[0]

    with open(arquivo + '.txt', 'w') as a:
        a.write(dados)


def ler_arquivo():
    arquivo = QtWidgets.QFileDialog.getOpenFileName()[0]

    with open(arquivo, 'r') as a:
        tela.label_5.setText(a.read())


app = QtWidgets.QApplication([])
tela = uic.loadUi('menu_salvar.ui')

tela.actionSalvar.triggered.connect(salvar)
tela.actionAbrir.triggered.connect(ler_arquivo)

tela.show()
app.exec()

