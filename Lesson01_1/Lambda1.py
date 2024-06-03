def f1(x, y):
    return x * y


result = f1(2, 4)
print(f"result={result}, type={type(f1)}")

f2 = lambda x, y: x * y
result = f2(2, 3)
print(f"result={result}, type={type(f2)}")
