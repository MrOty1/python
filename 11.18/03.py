for sk in range(10000, 100000):
    pirmidu = sk // 1000
    paskutiniaidu = sk % 100
    pirmusum = (pirmidu // 10) + (pirmidu % 10)
    paskutiniusand = (paskutiniaidu // 10) * (paskutiniaidu % 10)
    if pirmusum == paskutiniusand:
        print(sk, end=', ')