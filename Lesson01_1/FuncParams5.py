def func1(x, y=2):
    return x, y, x * y


x, y, result = func1(12, 4)
print(f'Func {x} * {y} = {result}')
x, y, result = func1(12)
print(f'Func {x} * {y} = {result}')
