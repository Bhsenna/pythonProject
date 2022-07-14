from Conta import ContaPoupanca, ContaCorrente

cc = ContaCorrente('Bradesco', '2407', 'Hazime', 1000)
cc.sacar(1100)
cc.depositar(1000)
cc.sacar(300)
cp = ContaPoupanca('Bradesco', '2407', 'Hazime', 1000)
cp.sacar(1200)