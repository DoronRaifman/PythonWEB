a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
print(f'a: {a}')
print(f'b: {b}')
x = zip(a, b)
print(f'note that zip is generator {x}')
xt = tuple(x)
print(f'tup {xt}')

