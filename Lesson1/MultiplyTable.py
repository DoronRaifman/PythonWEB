def get_multiply_matrix():
    multiply_table = []
    for i in range(1, 10+1):
        row = []
        for j in range(1, 10+1):
            row.append(f"{i*j:3d}")
        multiply_table.append(row)
    return multiply_table


def get_multiply_matrix_nice():
    multiply_table = []
    for i in range(1, 10 + 1):
        multiply_table.append([f"{i*j:3d}" for j in range(1, 10+1)])
    return multiply_table


def get_multiply_matrix_double_for():
    return [[f"{i*j:3d}" for j in range(1, 10+1)] for i in range(1, 10+1)]


if __name__ == '__main__':
    multiply_matrix = get_multiply_matrix_double_for()
    for row in multiply_matrix:
        print(row)
    print('slicing')
    for row in multiply_matrix[2:5]:
        print(row[5:7])

