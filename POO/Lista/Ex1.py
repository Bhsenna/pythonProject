class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self, nova_cor):
        print(f'Cor trocada de {self.cor} para {nova_cor}')
        self.cor = nova_cor

    def mostrar_cor(self):
        print(self.cor)


b1 = Bola('Azul', 'Grande', 'Elastico')
b1.mostrar_cor()
b1.trocar_cor('Vermelho')
b1.mostrar_cor()