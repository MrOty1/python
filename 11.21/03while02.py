# Petriukas ir pazymiai

kiek = int(input('Kiek pazymiu: '))
kelintas = 0
suma = 0
while kelintas < kiek:
    paz = int(input(f'Iveskite {kelintas + 1}-ajį pazymį: '))
    if not(1<=paz<=10):
        print(f'{paz} - blogai viesti duomenys')
        continue
    suma = suma + paz
    kelintas = kelintas + 1

vidurkis = suma / kelintas

print(f'Vidurkis: {vidurkis}')