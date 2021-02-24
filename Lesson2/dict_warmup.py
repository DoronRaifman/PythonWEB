def add_values_as_key(dict1, dict2):
    keys = set(list(dict1.keys()) + list(dict2.keys()))
    return {key: (dict1[key] if key in dict1 else 0) +
                 (dict2[key] if key in dict2 else 0) for key in keys}


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
print(add_values_as_key(d1, d2))



