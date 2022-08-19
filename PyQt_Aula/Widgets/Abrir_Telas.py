from PyQt5 import uic, QtWidgets


def chama_segunda_tela():
    segunda_tela.show()


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi('tela1.ui')
segunda_tela = uic.loadUi('tela2.ui')
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)

primeira_tela.show()
app.exec()

