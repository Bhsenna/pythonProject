class Animal:
    def __init__(self, altura: float, comprimento: float, peso: float, habitat):
        self.altura = altura
        self.comprimento = comprimento
        self.peso = peso
        self.habitat = habitat
        self.energia = 5
        self.estomago = []

    def comer(self, alimento):
        print('NHAC')
        self.energia -= 1
        self.estomago.append(alimento)

    def digerir(self):
        print('Blerg')
        self.energia += len(self.estomago)
        self.estomago.clear()

    def dormir(self):
        print('A mimir')
        self.energia += 1

    def locomover(self):
        print('Se moveu')
        self.energia -= 1


class Felinos(Animal):
    def __init__(self, altura: float, comprimento: float, peso: float, habitat, afiacao_das_garras: int, garras_fora: bool):
        super().__init__(altura, comprimento, peso, habitat)
        self.garras = garras_fora
        self.afiacao = afiacao_das_garras

    def afiar(self):
        self.afiacao += 25
        if self.afiacao > 100:
            self.afiacao = 100
        print(f'Garras {self.afiacao}% afiadas')

    def toggle_garras(self):
        if self.garras:
            print('Garras retraídas')
            self.garras = False
        else:
            print('Garras expandida')
            self.garras = True


class Caninos(Animal):
    def __init__(self, altura: float, comprimento: float, peso: float, habitat, sociavel: bool, garras_fora=False):
        super().__init__(altura, comprimento, peso, habitat)
        self.garras = garras_fora
        self.sociabilidade = sociavel

    def toggle_garras(self):
        if self.garras:
            print('Garras retraídas')
            self.garras = False
        else:
            print('Garras expandida')
            self.garras = True

    def socializar(self):
        if self.sociabilidade:
            print('Fez amiguinhos, e formou uma matilha!')
        else:
            print('Conheceu outros, mas logo se separaram')


class Cnidarios(Animal):
    def __init__(self, altura: float, comprimento: float, peso: float, habitat, medusa: bool, polipo: bool, estomago_cheio = False):
        super().__init__(altura, comprimento, peso, habitat)
        if medusa and polipo:
            print('Erro, mão pode ser Medusa e Pólipo ao mesmo tempo')
        else:
            self.medusa = medusa
            self.polipo = polipo
        self.estomago = estomago_cheio

    def comer(self, alimento):
        if self.estomago:
            print('Já está cheio!')
        else:
            print('Shlomp')
            self.energia -= 1
            self.estomago = True

    def digerir(self):
        print('EUA')
        self.energia += 1
        self.estomago = False


class Humano(Animal):
    def __init__(self, altura: float, comprimento: float, peso: float, habitat, gay: bool, qi: int):
        super().__init__(altura, comprimento, peso, habitat)
        self.gay = gay
        self.QI = qi

    def minino_esperto(self):
        if self.QI >= 90:
            print('Seu QI é deveras maior de grande')
        else:
            print('Seu bobinho')

    def mano_tu_eh(self):
        if self.gay:
            print('Sou não, tava só testando ele')
        else:
            print('Sou não, tava só testando ele')