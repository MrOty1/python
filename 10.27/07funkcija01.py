# sk1 = int(input('sk1 = ..... '))
# sk2 = int(input('sk2 = ..... '))
# suma = sk1 + sk2
# print(f'{sk1} + {sk2} = {suma}')

def calculator(txt):
    sk = int(input(txt))
    return sk

def total(a, b):
    result = a + b
    return result

def result():
    sk1 = calculator('sk1 = ..... ')
    sk2 = calculator('sk2 = ..... ')
    suma = total(sk1, sk2)
    print(f'{sk1} + {sk2} = {suma}')

result()