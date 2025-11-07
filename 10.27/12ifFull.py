# if salyga arba loginis reiskinys:
#     veiksmas kai salyga teisinga
# else:
#     veiksmai kai salyga klaidinga

# Nustatyti ar skaicius lyginis, jei lyginis atspausdinti jo kvadrata, jei nelyginis kuba
sk = int(input('sk = '))
if sk % 2 != 0:
    print(f'Skaicius {sk} nelyginis')
    ats = sk**3
    print(f'{ats}')
else:
    print(f'Skaicius {sk} lyginis')
    ats = sk**2
    print(f'{ats}')
print(f'Atlikus veiksmus gavom {ats}')