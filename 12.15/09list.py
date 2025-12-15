m = [4, 8, 7, 9, 7, 4, 5, 8, 9, 1, 8, 4, 1, 9, 7, 3]
mLyginis = []
sumaLyg = 0

# for i in m:
#     if i % 2 == 0:
#         mLyginis.append(i)
#         sumaLyg += i

sumaLyg = sum(i for i in m if i % 2 == 0)

print(sumaLyg)