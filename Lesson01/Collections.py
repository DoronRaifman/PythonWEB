tuple1 = (1, 2, 3, 'string1')
print(f'tuple: {tuple1}')
list1 = [1, 2, 3, 'string1']
print(f'list: {list1}')
dict1 = {1: 1, 2: 2, 3: 3, 'string1': 'string1', (1, 2): 'tuple'}
print(f'dict: {dict1}')

list1.append(tuple1)
print(f'list after append: {list1}')
list2 = [8, 7, 6] + list1
print(f'list after concatenate: {list2}')
print(f'indexing list: {list2[3]}')
print(f'indexing tuple: {tuple1[3]}')
print(f'indexing using - : {list1[-1]}')
list1[-1] = 12
print(f'assignment: {list1}')
print(f'dict lookup: {dict1["string1"]}, {dict1[3]}')
dict1['string1'] = 'other string'
dict1[3] = 7
print(f'dict assignment: {dict1}')


