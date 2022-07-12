class Veiculo:
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo):
        self.cor = cor
        self.lugares = lugares
        self.qtd_pneus = qtd_pneus
        self.tipo_motor = tipo_motor
        self.valor = valor
        self.ano = ano
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print('Vroom Vroom')

    def frear(self):
        print('Skrrr')

    def ligar(self):
        print('Ligou')

    def desligar(self):
        print('Desligou')


class Moto(Veiculo):
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo, empinada=False):
        super().__init__(cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo)
        self.empinada = empinada

    def empinar(self):
        if self.empinada:
            print('Já está empinada')
        else:
            print('RANDAMDAMDAMDAM')
            self.empinada = True

    def desempinar(self):
        self.empinada = False


# Criar uma classe herdeira Carro, e outra Ônibus
# As 2 classes novas precisam ter 2 métodos novos e 2 atributos novos cada

class Carro(Veiculo):
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo, porta_aberta=False, farol=False):
        super().__init__(cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo)
        self.porta_aberta = porta_aberta
        self.farol = farol

    def abrir_porta(self):
        if self.porta_aberta:
            print('A porta já está aberta')
        else:
            print('Porta abrida')
            self.porta_aberta = True

    def fechar_porta(self):
        if self.porta_aberta:
            print('Porta fechada')
            self.porta_aberta = False
        else:
            print('A porta já está fechada')

    def toggle_farol(self):
        if self.farol:
            print('Farol desligado')
            self.farol = False
        else:
            print('Farol ligado')
            self.farol = True


class Busao(Veiculo):
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo, porta_aberta=False, lotado=True):
        super().__init__(cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo)
        self.porta_aberta = porta_aberta
        self.lotado = lotado

    def abrir_porta(self):
        if self.porta_aberta:
            print('A porta já está aberta')
        else:
            print('Tsss, Porta abrida')
            self.porta_aberta = True

    def fechar_porta(self):
        if self.porta_aberta:
            print('Tsss, Porta fechada')
            self.porta_aberta = False
        else:
            print('A porta já está fechada')

    def lotacao(self):
        if self.lotado:
            print('ônibus genérico')
        else:
            print('Vai jogar na loteria')