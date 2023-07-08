tuple1 = (1, 2, 3, 4, 5, 6)
print(f'tuple: {tuple1}')
print(f'simple slicing: {tuple1[0:2]}')
print(f'slicing 2: {tuple1[3:]}')
print(f'slicing 3: {tuple1[3:-1]}')
print(f'slicing 4: {tuple1[:3]}')
print(f'slicing 5: {tuple1[::2]}')
print(f'slicing 6: {tuple1[::-1]}')
print(f'slicing 7: {tuple1[::-2]}')
print(f'slicing 8: {tuple1[2::-2]}')
print(f'slicing 9: {tuple1[2:-1:-2]}')
list1 = list(tuple1)
list1[1:3] = [10]
print(f'assignment slicing: {list1}')
my_name = 'Doron'
print(f'str slicing: {my_name[::-1]}')
tuple2 = [1, 2, 3, 4, 7, 1, 3, 8, 12, 4, (1, 2, 3)]
# print(f'exercise: {tuple2[-1][-2:]}')
