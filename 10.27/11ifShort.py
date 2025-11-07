# if salyga arba loginis reiskinys:
#     veiksmas kai salyga teisinga
# else:
#     veiksmai kai salyga klaidinga

# sutrumpintas if
# apskaiciuoti skaiciaus kvadrata jei skaicius lygus 13 isvesti pranesima laimingas skaicius
# bet kvadrata apskaiciuoti
sk = int(input('sk = .....'))
kv = sk**2
if sk == 13:
    print('laimingas skaicius.....')
    print('bet kv skaiciuosim')
print(f'skaicius {sk} pakelius kvadratu gausim {kv}')