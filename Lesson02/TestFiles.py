with open('TextFile.txt', 'wt') as fdes:
    for i in range(1, 10 + 1):
        row = [f'{i*j:4d}' for j in range(1, 10+1)]
        row_line = ''.join(row) + '\n'
        fdes.write(row_line)
