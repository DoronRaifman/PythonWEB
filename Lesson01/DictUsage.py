def using_items(my_dict):
    print('using items()')
    line = ''
    for key, val in my_dict.items():
        line += f'{key}: {val}, '
    print('{' + line + '}')


def using_keys(my_dict):
    print('using keys()')
    line = ''
    for key in my_dict.keys():
        val = my_dict[key]
        line += f'{key}: {val}, '
    print('{' + line + '}')


def using_values(my_dict):
    print('using values()')
    values = list(my_dict.values())
    print(f'values: {values}')
    print(f'sorted values')
    print(f'values: {sorted(values)}')


if __name__ == '__main__':
    my_dict = {i: 10 - i for i in range(1, 10+1)}
    using_items(my_dict)
    using_keys(my_dict)
    using_values(my_dict)

