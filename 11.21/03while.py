# Petriukas ir pazymiai

kiek = int(input('Kiek pazymiu: '))
kelintas = 0
suma = 0
while kelintas < kiek:
    kelintas = kelintas + 1
    paz = int(input(f'Iveskite {kelintas}-ajį pazymį: '))
    if 1<=paz<=10:
        suma = suma + paz
    else:
        print(f'{paz} - blogai viesti duomenys')
        kelintas = kelintas - 1

vidurkis = suma / kelintas
print(vidurkis)