

def func(input_list: list) -> list:
    result_list = {list(item.values())[0] for item in input_list}
    return list(sorted(result_list))


if __name__ == '__main__':
    list1 = [
        {"V": "S001"}, {"V1": "S002"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"},
    ]
    result = func(list1)
    print(f'func result: {result}')
