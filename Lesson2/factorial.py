
def factorial(n):
    res = n * factorial(n-1) if n > 1 else 1
    return res


n = 3
res = factorial(n)
print(f'n:{n}, res:{res}')
