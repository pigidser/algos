import math
import matplotlib.pyplot as plt
import numpy as np


task = 7

if task == 1:
    # 1 - y1 растет не быстрее y2 - False
    n = np.linspace(1, 20, 20)
    y1 = n.copy()
    for i, v in enumerate(n):
        y1[i] = math.factorial(v)
    y2 = 2**(n)

elif task == 2:
    # 2 - y1 растет не медленнее y2 - True
    n = np.linspace(1, 1000, 10)
    y1 = n**2 / ( np.log(n) / np.log(3) )
    y2 = n * ( np.log(n) / np.log(2) )**2

elif task == 3:
    # 3 - y1 растет одинаково с y2 - True
    n = np.linspace(1, 20, 50)
    y1 = 2**n
    y2 = 2**(n+1)

elif task == 4:
    # 4 - y1 растет одинаково с y2 - False
    n = np.linspace(1, 30, 50)
    y1 = n**(1/2)
    y2 = 5**( np.log(n) / np.log(2) )

elif task == 5:
    # 1 - y1 растет одинаково с y2 - False
    n = np.linspace(1, 20, 20)
    y1 = n.copy()
    for i, v in enumerate(n):
        y1[i] = math.factorial(v)
    y2 = 2**(n)

elif task == 6:
    # 1 - y1 растет не медленнее y2 - True
    n = np.linspace(1, 20, 20)
    y1 = n.copy()
    for i, v in enumerate(n):
        y1[i] = math.factorial(v)
    y2 = 2**(n)

elif task == 7:
    # 7 - True - растет одинаково с y2 - False
    n = np.linspace(1, 30, 50)
    y1 = n * (2**n)
    y2 = 3**n

# print(n)
print(y1[-5:])
print(y2[-5:])
# plot
fig, ax = plt.subplots()

ax.plot(n, y1, linewidth=2.0)
ax.plot(n, y2, linewidth=2.0)
ax.legend(['y1', 'y2'])


plt.show()
