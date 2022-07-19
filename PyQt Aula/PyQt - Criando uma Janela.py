import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Janela(QMainWindow):  # Classe para o Objeto da Janela
    def __init__(self):  # Método construtor
        super().__init__()  # Chamar a Super-Classe

        # Parâmetro de Posição da Janela  -  Mesma lógida do PyAutoGUI
        self.topo = 100
        self.esquerda = 100
        # Parâmetro de Tamanho da Janela
        self.largura = 800
        self.altura = 600
        # Parâmetro de Nome da Janela
        self.titulo = 'Primeira Janela'

        # Chama a Função de carregar a Janela
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)  # Constroi a janela com os Parâmetros dados
        self.setWindowTitle(self.titulo)  # Define o Título da janela
        self.show()  # Mostra a janela


aplicacao = QApplication(sys.argv)  # Intancia uma Aplicação do PyQt
janela = Janela()  # Instancia um objeto da Janela
sys.exit(aplicacao.exec_())  # Roda a Aplicação