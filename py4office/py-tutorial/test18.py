import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([0, 100])
plt.plot(xpoints, ypoints, 'k:')
# plt.show() 这行run之后可以显示出来图形

# data = np.arange(10)
# plt.plot(data)

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

plt.plot(np.random.randn(50).cumsum(), 'k--')   #'k--'表示黑色分段线
_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha = 0.3)

