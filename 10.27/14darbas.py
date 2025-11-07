# IVEDAMI DU SKAICIAI a, b
# kintamasis did priskirtas didesni skaiciu
# kintamasis maz priskirtas mazesni skaiciu
# jei lygus atspausdinti lygus max min nenaudoti

a = int(input('a = '))
b = int(input('b = '))

if a > b:
    did = a
    maz = b
    print(f'maz = {maz}, did = {did}')
elif a < b:
    did = b
    maz = a
    print(f'maz = {maz}, did = {did}')
else:
    print(f'{a} lygus {b}')