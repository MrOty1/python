# Ivedimas bet koks skaicius rasti to skaiciaus skaitmenu suma
#12345 ---> 15
#12345 % 10 = 5 12345 // 10 = 1234 % 10 = 4 1234 // 10 = 123 % 10

sk = int(input('Skaičius: '))
suma = 0
kopija = sk
while sk > 0:
    x1 = sk % 10
    suma+= x1
    sk //= 10 #sk = sk // 10
print(f'skaičiaus {kopija} skaitmenu suma = {suma}')