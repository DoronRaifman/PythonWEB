import numpy as np


def get_multiply_matrix():
    multiply_matrix = []
    for i in range(1, 10+1):
        row = np.linspace(i*1, i*10, 10)
        multiply_matrix.append(row)
    multiply_matrix = np.array(multiply_matrix, dtype=np.int)
    return multiply_matrix


def get_multiply_matrix_nice():
    return np.array([np.linspace(i*1, i*10, 10, dtype=np.int) for i in range(1, 10+1)])


# no python loops
def get_multiply_matrix_numpy():
    vector = np.arange(1, 10+1, dtype=np.int)
    # wtf = vector[:, None]
    return vector * vector[:, None]


def get_multiply_matrix_numpy_outer():
    vector = np.arange(1, 10+1, dtype=np.int)
    return np.outer(vector, vector)


def get_multiply_matrix_numpy_simple():
    vector = np.arange(1, 10+1, dtype=np.int)
    mtx = np.tile(vector, (10, 1)).transpose()
    return vector * mtx


if __name__ == '__main__':
    multiply_matrix = get_multiply_matrix_numpy_simple()
    # multiply_matrix = get_multiply_matrix_numpy()
    print(multiply_matrix)
    print(multiply_matrix[2:5, 5:7])
    print(np.where(multiply_matrix <= 50, multiply_matrix, -1))

