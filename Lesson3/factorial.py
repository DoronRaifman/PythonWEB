def factorial(n):
    return(n * factorial(n-1) if n > 1 else 1)


n = 3
res = factorial(n)
print(f'n:{n}, res:{res}')
