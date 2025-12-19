for sk in range(1000, 10000):
    pirmidu = sk // 100
    paskutiniaidu = sk % 100
    apverstipirmi = (pirmidu % 10) * 10 + (pirmidu // 10)
    if apverstipirmi == paskutiniaidu:
        print(sk, end=', ')