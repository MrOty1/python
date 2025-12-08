n = int(input('N = '))

# for i in range(n):
#     for j in range(n):
#         print(j, end=' ')
#     print('')


for i in range(n):
    for j in range(i + 1):
        print(j, end=' ')
    print('')