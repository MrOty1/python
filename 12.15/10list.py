m = [-4, -8, -7, 9, -7, -4, -5, -8, -9, -1, -8, -4, -1, -9, -7, 3]
print(m)
print(max(m))
print(min(m))

sarNeig = [i for i in m if i < 0]
print(sarNeig)
print(max(sarNeig))
print(min(sarNeig))

maxNeig = max(i for i in m if i < 0)
print(maxNeig)

kiekNeig = len(list(i for i in m if i < 0))
print(kiekNeig)