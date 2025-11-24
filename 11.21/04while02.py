# Ivedimas bet koks skaicius rasti to skaiciaus skaitmenu suma
#12345 ---> 15
#12345 % 10 = 5 12345 // 10 = 1234 % 10 = 4 1234 // 10 = 123 % 10
def skaiciuok(skaicius):
    suma = 0
    while skaicius > 0:
        x1 = skaicius % 10
        suma+= x1
        skaicius //= 10 #sk = sk // 10
    return suma

sk = int(input('Skaičius: '))
rez = skaiciuok(sk)
print(f'Skaičiaus {sk} skaitmenų suma = {rez}')