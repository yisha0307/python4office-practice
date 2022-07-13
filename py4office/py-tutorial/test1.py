# fibonacci函数
from traceback import print_tb


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a+b
    print()

fib(50)

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

print(fib2(200))

# *name:接受一个包含除了已有形参列表以外的位置参数的元组的形参
# **name: 接受一个包含除了已有形参列表以外的位置参数的字典的形参
# *name需要在**name之前
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print('*'*40)
    for kw in keywords:
        print(kw, ':', keywords[kw])
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# 普通函数
def standard_arg(arg):
    print(arg)

# 仅限位置参数
def pos_only_arg(arg, /):
    print(arg)

#仅限关键字参数
def kw_only_arg(*, arg):
    print(arg)