def func1(my_list):
    for i, val in enumerate(my_list):
        print(f'{i}: {val}')


if __name__ == '__main__':
    my_list = list(range(1, 10+1))
    func1(my_list)
