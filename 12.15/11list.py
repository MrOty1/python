sar = [4, -8, 7, -9, -7, 4, 5, 8, -9, -1, 8, -4, 1, -9, -7, 3]
nrNeig = []

# for i in range(len(sar)):
#     if sar[i] < 0:
#         nrNeig.append(i)

nrNeig = [i for i in range(len(sar)) if sar[i] < 0]

print(nrNeig)