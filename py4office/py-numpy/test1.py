import numpy as np

my_array = np.array([1,2,3,4,5])
print(my_array)
print(my_array.shape)

my_random_array = np.random.random(5)
print(my_random_array)

my_2d_array = np.zeros((2,3))  # 二维数组
print(my_2d_array)

array2 = np.array([[4,5], [6,7]])
print(array2, '*'*10, array2[1][1], array2.shape)
print(array2[:, 1])  # 提取第二列（索引1）的所有元素，即[5, 7]
print(array2[0,:])

# numpy中的数组操作
a = np.array([[1.0, 2.0], [3, 4]])
b = np.array([[5,6], [7,8]])
sum = a+b
difference = a-b
p = a * b
q = a / b
print('+:', sum)
print('-:', difference)
print('*:', p)
print('/:', q)

print(np.arange(5))
print('-'*40)

a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])

print(a)
print('-'*40)
print(a[:, 2])
print(a[0, 1:5])
print(a[::2, ::2])  # 被2整除的行和列

c = np.arange(25)
c = c.reshape(5,5)

d = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
              4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
              56, 3, 56, 44, 78])
d = d.reshape(5,5)
print('-'*40)
print(c,d)
print(c.dot(d))

a = np.arange(5, 100, 10)
print(a)
indices = [1, 5, -1]
print(a[indices])

aa = np.linspace(0, 2*np.pi, 50)
print(aa)
