import matplotlib

import matplotlib.pyplot as plt
import numpy as np


# x = np.array(["J", "O", "I", "L", "S", "O", "N"])
# y = np.array(["G", "O", "S", "T", "O", "S", "O"])
# plt.bar(x, y, color="red)
# plt.barh(x, y)
# plt.show()


# x = np.array(["A", "B", "C", "D", "E"])
# y = np.array([3, 8, 1, 10, 11])
# plt.scatter(x, y)
# plt.show()

# x = np.random.normal(170, 170, 170)
# plt.hist(x)
# plt.show()

# y = np.array([35, 25, 25, 15])
# mylables = ["joilson", "gostoso", "perfeito", "deus"]
# myexplode = [0.2, 0, 0, 0]
# plt.pie(y, labels=mylables, explode=myexplode, shadow=True)
# plt.show()


# x = np.array([3, 4, 5, 6, 8, 9, 11])
# y = np.array([12, 3, 5, 7, 8, 4, 2])
# plt.figure(figsize=(10, 10))
# plt.plot(x, y)
# plt.xlabel("cute")
# plt.ylabel("dangerous", size="15", color="red")
# plt.title("num")
# plt.suptitle("capybra")
# plt.grid(axis="x", color="green", linestyle="--", linewidth=0.2)
# plt.box(True)
# plt.show()

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.show()

y1 = [2, 3, 4.5]
y2 = [1, 1.5, 5]
plt.subplot(1, 1, 1)
plt.plot(y1)
plt.plot(y2)
plt.legend(["Azul", "Laranja"], loc="lower right")
plt.show()
#
# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]
# plt.subplot(1, 2, 2)
# plt.plot(x, y)
# plt.legend(['Legenda'])
# plt.show()