def hanoi(n, src, use, dst):
    # print(f'hanoi:n={n}, src:{src}, use:{use}, dst:{dst}')
    if n == 1:
        print(f'-> move1_1:n={n}, move from {src} to {dst}')
    else:
        hanoi(n-1, src, dst, use)
        print(f'-> move1_2:n={n}, move from {src} to {dst}')
        hanoi(n-1, use, dst, src)


if __name__ == '__main__':
    hanoi(3, 'orig', 'help', 'dest')

