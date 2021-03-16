import timeit


if __name__ == '__main__':
    n = 10
    print(f'n={n}')
    result1 = [i for i in range(1, n+1)]
    print(f'List Comprehension={result1}')
    result2 = (i for i in range(1, n+1))
    print(f'generator={result2}\n{tuple(result2)}')
    result3 = [i for i in range(1, n+1) if i % 2 == 0]
    print(f'List Comprehension Zugi={result3}')
    result4 = {i:i*i for i in range(1, n+1)}
    print(f'Dict Comprehension {result4}')
    time1 = timeit.timeit('[i for i in range(1, n+1)]', setup='n=10', number=10000)
    time2 = timeit.timeit('tuple(i for i in range(1, n+1))', setup='n=10', number=10000)
    print(f'times: listcomp:{time1:.3f}, generator:{time2:.3f}')
