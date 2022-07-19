import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip


class Janela(QMainWindow):  # Classe para o Objeto da Janela
    def __init__(self):  # Método construtor
        super().__init__()  # Chamar a Super-Classe

        # Parâmetro de Posição da Janela  -  Mesma lógida do PyAutoGUI
        self.topo = 100
        self.esquerda = 300
        # Parâmetro de Tamanho da Janela
        self.largura = 800
        self.altura = 600
        # Parâmetro de Nome da Janela
        self.titulo = 'Primeira Janela'

        # Intancia um Botão
        botao1 = QPushButton('Botao1', self)
        botao1.move(150, 200)  # Define a Posição do Botão  -  Mesma lógida do PyAutoGUI
        botao1.resize(150, 80)  # Define o Tamanho do Botão  -  (Largura, altura)
        botao1.setStyleSheet('QPushButton {background-color:#b427d3;font:bold;font-size:20px}')  # Altera a aparencia do Botão  -  Usa programação em CSS
        botao1.clicked.connect(self.botao1_click)  # Quando botão for clicado, realiza a Função dada (deve ser colocada com self. e sem parenteses)

        botao2 = QPushButton('Botao2', self)
        botao2.move(400, 200)
        botao2.resize(150, 80)
        botao2.setStyleSheet(
            'QPushButton {background-color:#27d3cd;font:bold;font-size:20px}')
        botao2.clicked.connect(self.botao2_click)

        # Chama a Função de carregar a Janela
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)  # Constroi a janela com os Parâmetros dados
        self.setWindowTitle(self.titulo)  # Define o Título da janela
        self.show()  # Mostra a janela

    def botao1_click(self):
        print('O botao 1 foi clicado!')

    def botao2_click(self):
        print('O botao 2 foi clicado!')

aplicacao = QApplication(sys.argv)  # Intancia uma Aplicação do PyQt
janela = Janela()  # Instancia um objeto da Janela
sys.exit(aplicacao.exec_())  # Roda a Aplicação