class Retangulo:
    def __init__(self, comprimento, altura):
        self.comprimento = comprimento
        self.altura = altura

    def mudar_comprimento(self, novo_comprimento):
        print(f'Comprimento alterado de {self.comprimento} para {novo_comprimento}')
        self.comprimento = novo_comprimento

    def mudar_altura(self, nova_altura):
        print(f'Altura alterada de {self.altura} para {nova_altura}')
        self.altura = nova_altura

    def valor(self):
        print(f'Comprimento: {self.comprimento}\nAltura: {self.altura}')

    def area(self):
        print(f'Area igual a {self.comprimento * self.altura}')

    def perimetro(self):
        print(f'Perimetro igual a {self.comprimento * 2 + self.altura * 2}')


