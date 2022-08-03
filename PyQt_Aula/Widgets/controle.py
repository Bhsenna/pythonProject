from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt


def listar_dados():
    dado_lido = janela.lineEdit.text()
    if not janela.listWidget.findItems(dado_lido, Qt.MatchExactly):
        janela.listWidget.addItem(dado_lido)
    janela.lineEdit.setText('')


def deletar():
    janela.listWidget.clear()


app = QtWidgets.QApplication([])
janela = uic.loadUi("lista.ui")
janela.pushButton.clicked.connect(listar_dados)
janela.pushButton_2.clicked.connect(deletar)

janela.show()
app.exec()