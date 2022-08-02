from PyQt5.QtWidgets import QApplication, QLabel  # Importa as funções do PyQt
app = QApplication([])  # Cria uma instância do PyQt, requerida pelo GUI
# Dentro dos [] fica os parâmetros e linhas de comando
label = QLabel('Hello World!')  # Cria um objeto na janela do PyQt
label.show()  # Insere o objeto dentro da janela do PyQt
app.exec()  # Entrega o controle ao Qt, permitindo que a janela permaneça aberta até o usuário fechar
