import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 2*np.pi, 50)
b = np.sin(a)

plt.plot(a, b)
mask = b >= 0
plt.plot(a[mask], b[mask], 'bo')
mask = (b>=0) &(a <= np.pi /2)
plt.plot(a[mask], b[mask], 'go')
plt.show()

# 缺省索引
a= np.arange(0, 100, 10)
b = a[:5]
c = a[a>=50]
print(b)
print(c)