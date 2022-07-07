# Criar uma classe para uma lata de coca-cola.
# A classe deve ter todos os atributos dimensionais,
# e suas características de material.
# As funcionalidades(métodos) da garrafa sao, abrir,
# beber, esvaziar, amassar, retirar lacre, e descartar
class Lata:
    def __init__(self, altura, diametro, volume, material, rotulo):
        self.altura = altura
        self.diametro = diametro
        self.volume = volume
        self.material = material
        self.rotulo = rotulo

    def abrir(self):
        print(f'Tchi, latinha de {self.rotulo} aberta!')

    def beber(self):
        print(f'Glub Glub, ahhhh {self.rotulo} deliciosa!')

    def esvaziar(self):
        print(f'Shhhhh, latinha de {self.rotulo} vazia')

    def amassar(self):
        print(f'Crunch, coitada da latinha de {self.rotulo}')

    def retirar_lacre(self):
        print(f'CLACK, lacre da {self.rotulo} retirado!')

    def descartar(self):
        print(f'Tchau Tchau, latinha de {self.rotulo}!')


lata1 = Lata(10, 5, 2, 'Alumínio', 'Coca-Cola')
lata1.retirar_lacre()
lata1.abrir()
lata1.beber()
lata1.amassar()
lata1.descartar()