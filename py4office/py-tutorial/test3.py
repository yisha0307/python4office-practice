a = list(range(0,20,2))
print(a)
b = list(range(20,0,-2))
print(b)

seq = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in seq:
    print('a={0}, b={1}, c={2}'.format(a,b,c))
