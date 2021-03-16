a = ('apple', 'banana', 'cherry')
print(f'a: {a}')
x = map(lambda val: len(val), a)
print(f'note that map is also generator {x}')
xt = tuple(x)
print(f'tup {xt}')

