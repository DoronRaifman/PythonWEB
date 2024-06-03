def func1(x, y):
    return x, y, x * y


x, y, result = func1(12, 4)
print(f'Func {x} * {y} = {result}')

params = {'x': 12, 'y': 4}
x, y, result = func1(**params)  # unpack dict on call
print(f'Func {x} * {y} = {result}')

