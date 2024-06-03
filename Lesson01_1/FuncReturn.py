def func1(x, y):
    return x, y, x * y


res = func1(10, 8)
print(f'Multiply result = {res}')
x, y, result = res  # unpacking
print(f'Multiply {x} * {y} = {result}')

