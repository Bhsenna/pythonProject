class Conta:
    def __init__(self, agencia, conta, saldo=0.0):
        self.agencia = agencia
        self.conta = conta
        self.__saldo = saldo  # adicionar o __ antes do nome torna o atributo inacessível de fora das defs

    def depositar(self, valor):
        self.__saldo += valor
        self.__mensagem()

    def ver_saldo(self):
        print(self.__saldo)

    def __mensagem(self): # adicionar o __ antes do nome torna o método inacessível de fora da classe
        print('Bom dia, seu depósito foi feito')


c1 = Conta(3365, '1234-5')
c1.ver_saldo()