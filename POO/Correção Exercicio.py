# Criar uma classe para uma lata de coca-cola.
# A classe deve ter todos os atributos dimensionais,
# e suas características de material.
# As funcionalidades(métodos) da garrafa sao, abrir,
# beber, esvaziar, amassar, retirar lacre, e descartar

class Lata:
    def __init__(self, altura, diametro, volume, material='aluminio', rotulo='coca'):
        self.altura = altura
        self.diametro = diametro
        self.volume = volume
        self.material = material
        self.rotulo = rotulo
        self.lacre = True
        self.amassada = False
        self.descartada = False
        self.aberta = False

    def abrir(self):
        if self.descartada:
            print('A latinha já foi descartada!')
        elif self.aberta:
            print('Já está aberta, seu bobinho')
        else:
            print('Lata foi aberta com sucesso')
            self.aberta = True

    def beber(self, quantidade):
        if self.descartada:
            print('A latinha já foi descartada!')
        elif not self.aberta:
            print('A lata está fechada, abra ela antes de beber')
        elif quantidade > self.volume:
            print(f'Você bebeu {self.volume}, e ainda faltou {quantidade-self.volume}')
            self.volume = 0
        else:
            self.volume -= quantidade
            print(f'Glub Glub, você bebeu {quantidade} e ainda tem {self.volume} na lata')

    def esvaziar(self):
        if self.descartada:
            print('A latinha já foi descartada!')
        elif not self.aberta:
            print('A lata está fechada, abra ela antes de esvaziar')
        elif not self.volume:
            print('A lata já está vazia!!')
        else:
            print('Latinha foi esvaziada!')
            self.volume = 0

    def amassar(self):
        if self.descartada:
            print('A latinha já foi descartada!')
        elif self.amassada:
            print('A latinha já está amassada')
        elif self.volume:
            print('A lata está cheia, vai escorre pra todo lado!')
        else:
            print('Crunch! Lata amassada.')
            self.amassada = True

    def retirar_lacre(self):
        if self.lacre:
            self.lacre = False
            print('TRECK, lacre removido')
        else:
            print('Não tinha lacre')

    def descartar(self):
        if self.descartada:
            print('A latinha já foi descartada!')
        elif not self.amassada:
            print('Amasse a latinha primeiro!')
        else:
            print('Tchau latinha!')
            self.descartada = True


l1 = Lata(12.22, 5.2, 350)
l1.abrir()
l1.beber(300)
l1.esvaziar()
l1.amassar()
l1.retirar_lacre()
l1.descartar()