for sk in range(100, 1000):
    a = sk // 100
    b = (sk // 10) % 10
    c = sk % 10
    suma = a + b + c
    sandauga = a * b * c
    if sandauga != 0 and suma % sandauga == 0:
        print(sk, end=', ')