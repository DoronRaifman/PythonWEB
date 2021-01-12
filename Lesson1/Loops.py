def func1(n):
    line = f'values: '
    for i in range(1, n+1):
        line += f'{i}, '
    line = line[:-2]
    return line


if __name__ == '__main__':
    n = 10
    result = func1(n)
    print(f'n={n}. result={result}')
