# sk1 = int(input('sk1 = ..... '))
# sk2 = int(input('sk2 = ..... '))
# suma = sk1 + sk2
# print(f'{sk1} + {sk2} = {suma}')

def calculator(txt):
    sk = int(input(txt))
    return sk

def total():
    a = calculator('sk1 = ..... ')
    b = calculator('sk2 = ..... ')
    result = a + b
    return result, a, b

def result():
    suma, sk1, sk2 = total()
    print(f'{sk1} + {sk2} = {suma}')

result()