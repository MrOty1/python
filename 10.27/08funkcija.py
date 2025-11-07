# 3 prekes reikia apskaiciuoti ju pvm (21%)

def taxes(*argz): #def func(*argzs, **argzs)
    print(type(argz))
    for i in argz:
        print(i)
    total = sum(argz)
    pvm = total * 0.21
    return pvm

p1 = 30
p2 = 5.25
p3 = 4.8
p4 = 5.14

pvmSize = taxes(p1, p2, p3, p4)
print(f'{pvmSize:.2f}')