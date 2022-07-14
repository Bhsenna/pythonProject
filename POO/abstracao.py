from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome, especie, habitat):
        self.habitat = habitat
        self.especie = especie
        self.nome = nome

    @abstractmethod  # Força a função a ser reescrita nas classes filhas
    def pedir_comida(self):
        return True

    def comer(self):
        print(f'{self.nome} comeu')

    @staticmethod
    def nascer():
        print('nasceu')

    @classmethod  # Permite que a função seja usada pela classe, sem instanciar um objeto
    def morrer(cls):
        print('morreu')


class Felinos(Animal, ABC):
    def __init__(self, nome, especie, habitat, garras, orelhas):
        super().__init__(nome, especie, habitat)
        self.garras = garras
        self.orelhas = orelhas

    def pedir_comida(self):
        print(f'Meow?')


gato = Felinos('Milka', 'Gato', 'Mato', True, 2)
gato.pedir_comida()
gato.comer()
Animal.morrer()