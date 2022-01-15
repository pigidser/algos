import math
import matplotlib.pyplot as plt
import numpy as np


task = 4

if task == 1 or task == 2:
    # 1 - True, 2 - False - y1 растет одинаково с y2
    n = np.linspace(100, 400, 50)
    y1 = 2**n
    y2 = 2**(n+1)

elif task == 3:
    # 3 - True - y1 растет не быстрее y2
    n = np.linspace(10, 50, 50)
    y1 = n * 2**n
    y2 = 3**n

elif task == 4:
    # 4 - True - y1 растет одинаково с y2
    n = np.linspace(100, 100000, 50)
    y1 = np.log(2*n) / np.log(3)
    y2 = np.log(3*n) / np.log(2)

elif task == 5:
    # 5 - True - y1 растет одинаково с y2
    n = np.linspace(1, 1000, 50)
    y1 = n**2 / ( np.log(n) / np.log(3) )
    y2 = n * ( np.log(n) / np.log(2) )**2

elif task == 6:
    # 6 - False - растет не быстрее
    n = np.linspace(1, 100000, 50)
    y1 = 10 * ( np.log(n) / np.log(2) )
    y2 = ( np.log(n) / np.log(2) )**2

elif task == 7:
    # 7 - True - растет не медленнее
    n = np.linspace(1, 100000, 50)
    y1 = 3*n + 5
    y2 = n

# print(n)
print(y1[-5:])
print(y2[-5:])
# plot
fig, ax = plt.subplots()

ax.plot(n, y1, linewidth=2.0)
ax.plot(n, y2, linewidth=2.0)
ax.legend(['y1', 'y2'])


plt.show()
