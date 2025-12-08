n = int(input('n: '))
sym = input('symbol: ')

# for i in range(n):
#     if i == 0 or i == n - 1:
#         for a in range(n):
#             print('*', end='')
#         print()
#     elif i != 0 or i != n:
#         print('* ', end='')
#         for b in range(n - 2):
#             print('', end=' ')
#         print('', end='*')
#         print()

for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 or i == 0 or i == n - 1:
            print(sym, end=' ')
        else:
            print(' ' * len(sym), end=' ')
    print()