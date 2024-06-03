list1 = [(10, 1), (4, 3), (9, 9), (0, 2)]
list_sorted1 = sorted(list1, key=lambda item: item[0])
list_sorted2 = sorted(list1, key=lambda item: item[1])
print(f"list1: {list1}")
print(f"list_sorted1: {list_sorted1}")
print(f"list_sorted2: {list_sorted2}")
