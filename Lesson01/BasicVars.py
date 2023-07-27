i = 7
print(f'i = {i}')
i = i + 5
print(f'i after add = {i}')
i -= 5
print(f'i after subtruct = {i}')
i /= 2
# note that divide i converted to float
print(f'i after divide = {i}')
i *= 4
print(f'i after multiply = {i}')
# integer divide as float
print(f'i after integer divide i = {i}, integer divide = {i // 3},'
      f' normal divide {i / 3:.2f}')
# demonstrate modulo
print(f'modulo: i = {i}, integer divide i//3:{i//3}, reminder i%3: {i%3}')
i = int(i)
print(f'i after convert to int = {i}')
j = 7.0
print(f'j as float = {j}')
my_name = 'Doron'
print(f'my_name as str = {my_name}')

