

def fibonacci_doron(n):
    result = [0, 1]
    while len(result) < n:
        result.append(result[-2] + result[-1])
    return result


def fibonacci_mishka(n):
    import functools as f
    fib = lambda n: f.reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
    return fib(n)


def fibonacci_ohad(n):
    result = [0,1]
    [result.append(result[-2]+result[-1]) for i in range(n)]
    return result


result = fibonacci_mishka(20)
print(f'fib: {result}')

