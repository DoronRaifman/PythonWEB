list1 = [1, 2, 3, 'string1', (1, 2, 3)]
list2 = list1
print('==> starting values:')
print(f'list 1: {list1}')
print(f'list 2: {list2}')
print('==> after slice set value:')
list2[-1] = (1, 2, 3, 4)
print(f'list 1: {list1}')
print(f'list 2: {list2}')
# making a copy before changing
print('==> after making copy '
      '(note slicer assignment result):')
list3 = list(list1)
list3[-1:] = (1, 2, 3)
print(f'list 1: {list1}')
print(f'list 3: {list3}')
