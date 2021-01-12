def generator(n):
    return [i for i in range(1, n+1)]


def generator_zugi(n):
    return [i for i in range(1, n+1) if i % 2 == 0]


if __name__ == '__main__':
    n = 10
    print(f'n={n}')
    result1 = generator(n)
    print(f'generator={result1}')
    result2 = generator_zugi(n)
    print(f'generator_zugi={result2}')
