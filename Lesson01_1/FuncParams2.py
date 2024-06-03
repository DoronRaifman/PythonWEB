def func1(**kwargs):
    print(f"kwargs={kwargs}")
    x, y = kwargs['x'], kwargs['y']
    return x, y, x * y


x, y, result = func1(x=12, y=4)
print(f'Func {x} * {y} = {result}')


