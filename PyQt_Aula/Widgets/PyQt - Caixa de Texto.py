import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5 import QtGui  # Módulo de Imagens


class Janela(QMainWindow):  # Classe para o Objeto da Janela
    def __init__(self):  # Método construtor
        super().__init__()  # Chamar a Super-Classe

        # Parâmetro de Posição da Janela  —  Mesma lógica do PyAutoGUI
        self.topo = 100
        self.esquerda = 300
        # Parâmetro de Tamanho da Janela
        self.largura = 800
        self.altura = 600
        # Parâmetro de Nome da Janela
        self.titulo = 'Primeira Janela'

        # Instancia uma caixa de texto
        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(25, 20)  # Define a Posição da Caixa de Texto  —  Mesma lógica do PyAutoGUI
        self.caixa_texto.resize(250, 50)  # Define o Tamanho da Caixa de Texto  —  (Largura, altura)

        # Instancia um Botão
        botao1 = QPushButton('Carro 1', self)
        botao1.move(150, 200)  # Define a Posição do Botão  —  Mesma lógica do PyAutoGUI
        botao1.resize(150, 80)  # Define o Tamanho do Botão  —  (Largura, altura)
        botao1.setStyleSheet('QPushButton {background-color:#b427d3;font:bold;font-size:20px}')  # Altera a aparência do Botão  —  Usa programação em CSS
        botao1.clicked.connect(self.botao1_click)  # Quando botão for clicado, realiza a Função dada (deve ser colocada com self. e sem parenteses)

        botao2 = QPushButton('Carro 2', self)
        botao2.move(350, 200)
        botao2.resize(150, 80)
        botao2.setStyleSheet('QPushButton {background-color:#27d3cd;font:bold;font-size:20px}')
        botao2.clicked.connect(self.botao2_click)

        botao_caixa = QPushButton('Enviar texto', self)
        botao_caixa.move(550, 200)
        botao_caixa.resize(150, 80)
        botao_caixa.setStyleSheet('QPushButton {background-color:#49cc19;font:bold;font-size:20px}')
        botao_caixa.clicked.connect(self.mostra_texto)

        # Instancia uma Label  —  Usar o self. permite que o Objeto seja acessado fora do __init__
        self.label_1 = QLabel(self)  # Instancia o Objeto de Label
        self.label_1.setText('Escolha o seu Carro!')  # Define o Texto da Label
        self.label_1.move(50, 100)  # Define a Posição da Label  —  Mesma lógica do PyAutoGUI
        self.label_1.setStyleSheet('QLabel {font:bold;font-size:25px}')
        self.label_1.resize(300, 25)  # Altera o Tamanho da Label, necessário para mostrar tod0 o Text

        self.label_caixa = QLabel(self)
        self.label_caixa.setText('Digitou: ')
        self.label_caixa.move(450, 100)
        self.label_caixa.setStyleSheet('QLabel {font:bold;font-size:25px}')
        self.label_caixa.resize(300, 25)

        # Criando uma Image
        self.carro = QLabel(self)  # Instancia o Objeto de Label
        self.carro.move(100, 300)  # Define a Posição da Label  —  Mesma lógica do PyAutoGUI
        self.carro.setPixmap(QtGui.QPixmap(''))  # Define a Label como Imagem, e seleciona a Imagem
        self.carro.resize(400, 200)

        # Chama a Função de carregar a Janela
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)  # Constrói a janela com os Parâmetros dados
        self.setWindowTitle(self.titulo)  # Define o Título da janela
        self.show()  # Mostra a janela

    def botao1_click(self):
        self.label_1.setText('Carro 1 selecionado!')
        self.label_1.setStyleSheet('QLabel {font:bold;font-size:25px;color:"#b427d3"}')
        self.carro.setPixmap(QtGui.QPixmap('Images/purple_car.png'))

    def botao2_click(self):
        self.label_1.setText('Carro 2 selecionado!')
        self.label_1.setStyleSheet('QLabel {font:bold;font-size:25px;color:"#27d3cd"}')
        self.carro.setPixmap(QtGui.QPixmap('Images/cyan_car.png'))

    def mostra_texto(self):
        conteudo = self.caixa_texto.text()  # Variável recebe o texto digitado dentro da Caixa de Texto
        self.label_caixa.setText('Digitou: ' + conteudo)  # Define o texto da Label como a varíavel 'conteudo'


aplicacao = QApplication(sys.argv)  # Instancia uma Aplicação do PyQt
janela = Janela()  # Instancia um objeto da Janela
sys.exit(aplicacao.exec_())  # Roda a Aplicação