import time
from datetime import datetime
import numpy as np


class NumpyLearn:
    def __init__(self):
        self.n = 1000000
        self.rows_count = 1000
        self.cols_count = 1000

    def main(self):
        # self.numpy_array()
        self.multiply_table()

    def numpy_array(self):
        # without list comprehension
        start_time = time.time()
        array1 = []
        for i in range(self.n):
            array1.append(i)
        diff = (time.time() - start_time) * 1000
        print(f'simple array: {diff:.0f} mSec')
        start_time = time.time()
        array2 = [i for i in range(self.n)]
        diff = (time.time() - start_time) * 1000
        print(f'list comprehension array: {diff:.0f} mSec')

        # numpy array
        start_time = time.time()
        array3 = np.array([i for i in range(self.n)])
        diff = (time.time() - start_time) * 1000
        print(f'numpy array 1: {diff:.0f} mSec')

        start_time = time.time()
        array4 = np.zeros(self.n, dtype=int)
        for i in range(self.n):
            array4[i] = i
        diff = (time.time() - start_time) * 1000
        print(f'numpy array 2: {diff:.0f} mSec')
        start_time = time.time()
        array5 = np.linspace(1, self.n, self.n, dtype=int)
        diff = (time.time() - start_time) * 1000
        print(f'numpy array 3: {diff:.0f} mSec')
        start_time = time.time()
        array6 = np.arange(1, self.n, 1, dtype=int)
        diff = (time.time() - start_time) * 1000
        print(f'numpy array 4: {diff:.0f} mSec')

    def multiply_table(self):
        # python version
        start_time = time.time()
        array1 = [[i*j for j in range(1, self.cols_count+1)] for i in range(1, self.rows_count+1)]
        array1_np = np.array(array1, dtype=str)
        diff = (time.time() - start_time) * 1000
        print(f'numpy array 1: {diff:.0f} mSec')
        # numpy version
        start_time = time.time()
        array2 = [np.linspace(row * self.cols_count, self.cols_count, self.cols_count, dtype=int)
                  for row in range(1, self.rows_count + 1)]
        array_np2 = np.array(array2, dtype=int)
        diff = (time.time() - start_time) * 1000
        print(f'numpy array 2: {diff:.0f} mSec')
        # numpy where
        start_time = time.time()
        array3 = np.where(array_np2 <= 50, array_np2, -1)
        diff = (time.time() - start_time) * 1000
        print(f'numpy where: {diff:.0f} mSec')


if __name__ == '__main__':
    numpy_learn = NumpyLearn()
    numpy_learn.main()

