def func1(x, y):
    return x, y, x * y


x, y, result = func1(x=10, y=8)
print(f'Func {x} * {y} = {result}')
x, y, result = func1(10, y=8)
print(f'Func {x} * {y} = {result}')

