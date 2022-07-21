import matplotlib.pyplot as plt

# plt.title("Gráfico de Alunos", size=15, color="red")
# eixox = ["Aprendizado Mínimo", "Aprendizado Médio", "Aprendizado Completo"]
# eixoy = [5.0, 20.0, 10.0]
# plt.xlabel("Aprendizado", color="green")
# plt.ylabel("Alunos", color="green")
# plt.bar(eixox, eixoy, color="grey")
# plt.grid(color="black", linestyle="-", linewidth=0.2)
# plt.show()

# plt.title("Padaria do Seu Jonas", size=15, color="red")
# aa = [30, 20, 10, 20, 15, 5]
# mylabels = ["pão", "bebidas", "balas e doces", "salgados", "bolos e cucas", "café"]
# myexplode = [0.2, 0, 0, 0, 0, 0]
# plt.pie(aa, labels=mylabels, explode=myexplode, shadow=True)
# plt.show()

plt.figure(figsize=(8, 8))
plt.title("Gráfico de Lucro por Mês das empresas Jonas e Reiter", color="red")
y1 = [10000, 20000, 30000, 2000, 12000]
y2 = [20000, 10000, 40000, 5, 8.50]
x = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio"]
plt.subplot(1, 1, 1)
plt.plot(y1)
plt.plot(x, y2)
plt.xlabel("Meses", color="r")
plt.ylabel("Lucro", color="r")
plt.legend(["Empresa jonas", "Empresa Reiter"], loc="upper right")
plt.grid(axis="y", color="black", linestyle="-", linewidth=0.1)
plt.show()

