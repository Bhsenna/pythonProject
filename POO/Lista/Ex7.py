class TV:
    def __init__(self, volume=10, canal=1):
        self.volume = volume
        self.canal = canal
        self.ligada = False

    def mudar_canal(self, canal: int):
        if 0 > canal or canal > 100:
            print('Esse canal não está disponível no seu plano atual!')
        else:
            self.canal = canal
            print(f'Canal alterado para {self.canal}')

    def aumentar_volume(self):
        if not self.ligada:
            print('A TV está desligada!')
        elif self.volume <= 100:
            self.volume += 1
            print(f'Volume: {self.volume}')
        else:
            print('Volume já está no máximo!')

    def diminuir_volume(self):
        if not self.ligada:
            print('A TV está desligada!')
        elif self.volume >= 0:
            self.volume -= 1
            print(f'Volume: {self.volume}')
        else:
            print('Volume já está no minimo!')

    def ligar_tv(self):
        if self.ligada:
            print('TV já está ligada!')
        else:
            print('A TV foi ligada!')
            self.ligada = True
            print(f'Canal: {self.canal}')
            print(f'Volume: {self.volume}')

    def desligar_tv(self):
        if self.ligada:
            print('TV foi desligada')
            self.ligada = False
            if input('Sair do sofá e fazer alguma coisa com a vida?\n').lower().startswith('s'):
                exit()
        else:
            print('A TV já está desligada!')
            if input('Sair do sofá e fazer alguma coisa com a vida?\n').lower().startswith('s'):
                exit()


from Funções.Lista.Func import getInt
tv = TV()
while True:
    acao = input('Você deseja:\n[1] Ligar TV\n[2] Desligar TV\n[3] Mudar o Canal\n[4] Aumentar o Volume\n[5] Diminuir o Volume\n')
    if acao == '1':
        tv.ligar_tv()
    elif acao == '2':
        tv.desligar_tv()
    elif acao == '3':
        if not tv.ligada:
            print('A TV está desligada!')
        else:
            tv.mudar_canal(getInt('Informe o canal: '))
    elif acao == '4':
        tv.aumentar_volume()
    elif acao == '5':
        tv.aumentar_volume()
    else:
        continue