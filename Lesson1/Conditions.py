response = input('Enter number:')
val = int(response)
if val > 10:
    if val % 2 == 0:
        print(f'{val} is large Zugi')
    else:
        print(f'{val} is large not Zugi')
else:
    if val % 2 == 0:
        print(f'{val} is small Zugi')
    else:
        print(f'{val} is small not Zugi')

# conditional assignment
result = val if val % 2 == 0 else 2 * val
print(f'result is {result}')


