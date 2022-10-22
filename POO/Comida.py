from Funções.Lista.Func import getFloat, getInt
tamanho_boca = 63.3


class Coisa():
    def __init__(self, nome, altura: float, comprimento: float, largura: float, fofura: int):
        self.nome = nome
        self.tamanho = altura * comprimento * largura
        if fofura >= 50:
            self.fofo = True
        else:
            self.fofo = False

    def eat(self):
        if self.tamanho < tamanho_boca:
            return f"{self.nome} foi comido!"
        else:
            return f"Você falhou em comer {self.nome}..."


object = Coisa(input('Insira o nome do objeto: '), getFloat('Insira a altura: '), getFloat('Insira o comprimento: '), getFloat('Insira a largura: '), getInt('Insira o nível de fofura: '))
if object.fofo:
    print(object.eat())
else:
    print(object.nome + ' não é fofo, não vale a pena comer')
