# Ivedamas pazymys. reikia nustatyti koks jis yra
# 1, 2, 3: Nepatenkinamas
# 4, 5, 6: Patenkinamas

paz = int(input('Koks pazymys: '))
match paz:
    case 1|2|3:
        rez = 'Nepatenkinamas'
    case 4|5|6:
        rez = 'Patenkinamas'
    case 7|8|9:
        rez = 'Geras'
    case 10:
        rez = 'Puiku'
    case _:
        rez = 'Blogai įvesti duomenys'

print(f'{paz} -----> {rez}')