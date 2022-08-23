from matplotlib import markers
import matplotlib
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np

# a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

# for i in a:
    # print(i)
plt.rcParams['font.family'] = ['PingFang HK']  # 设定中文字体
# zhfont = matplotlib.font_manager.FontProperties(fname="py4office/py-tutorial/data/SourceHanSansSC-Bold.otf") 
xpoints = np.array([0,6])
ypoints = np.array([0, 100])
plt.plot(xpoints, ypoints, 'k:')
plt.grid()  # 网格线
plt.title('医院分析', fontdict={'color': 'darkred', 'size': 15}, loc='left')
# plt.show() 这行run之后可以显示出来图形

# data = np.arange(10)
# plt.plot(data)

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax3.plot(np.random.randn(50).cumsum(), 'k--')   #'k--'表示黑色分段线
_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha = 0.3)

# 画在第二个subplot里
x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)
ax2.plot(x,y,x,z)

# 画在第四个subplot里
ypoints = np.array([1,3,4,5,8,9,6,1,4,4,2,6])
ax4.plot(ypoints, marker = 'o')

fig2 = plt.figure()
ax5 = fig2.add_subplot(2,2,1)
ax6 = fig2.add_subplot(2,2,2)
ax7 = fig2.add_subplot(2,2,3)
ax8 = fig2.add_subplot(2,2,4)

yy = np.array([6,2,13,10])
ax5.plot(yy, 'o:b',ms=2, ls='-.')

y1 = np.array([3,7,5,9])
y2 = np.array([6,2,13,10])
ax6.plot(y1)
ax6.plot(y2)

