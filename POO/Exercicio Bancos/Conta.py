from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero, nome, saldo=0):
        self.agencia = agencia
        self.numero = numero
        self.nome = nome
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def exibir_saldo(self):
        pass


class ContaCorrente(Conta, ABC):
    def __init__(self, agencia, numero, nome, saldo, limite=200):
        super().__init__(agencia, numero, nome, saldo)
        self.__limite = limite
        self.__saldo = saldo

    def sacar(self, valor):
        if valor <= (self.__saldo + self.__limite):
            self.__saldo -= valor
            print('Saque realizado')
        else:
            print('Limite ultrapassado')

        self.exibir_saldo()

    def exibir_saldo(self):
        print(f'{self.nome}, o seu saldo é de: R${self.__saldo:.2f}')

class ContaPoupanca(Conta, ABC):
    def __init__(self, agencia, numero, nome, saldo):
        super().__init__(agencia, numero, nome, saldo)
        self.__saldo = saldo

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print('Saque realizado')
        else:
            print('Saldo insuficiente')

        self.exibir_saldo()

    def exibir_saldo(self):
        print(f'{self.nome}, o seu saldo é de: R${self.__saldo:.2f}')