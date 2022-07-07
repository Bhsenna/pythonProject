class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        print(f'Tamanho do lado mudado de {self.lado} para {novo_lado}')
        self.lado = novo_lado

    def retornar_lado(self):
        print(f'Tamanho do lado é igual a {self.lado}')

    def area(self):
        print(f'A área é igual a {self.lado ** 2}')


q1 = Quadrado(2)
q1.retornar_lado()
q1.area()
q1.mudar_lado(4)
q1.retornar_lado()
q1.area()