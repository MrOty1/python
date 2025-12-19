for sk in range(1000000, 10000000):
    skaitmenys = []
    temp = sk
    for i in range(7):
        skaitmenys.append(temp % 10)
        temp = temp // 10
    suma = sum(skaitmenys)
    pirmutrijusand = skaitmenys[6] * skaitmenys[5] * skaitmenys[4]
    if suma == pirmutrijusand:
        print(sk, end=', ')