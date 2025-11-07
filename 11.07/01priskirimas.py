# Ivedu savaites dien skaiciumi 5 ----> penktadienis
# 7 ----> sekmadienis

diena = input('Iveskite savaites diena skaiciumi: ')
match diena:
    case '1':
        rez = 'Pirmadienis'
        print(f'Mes ivedeme {diena}')
        print('Tra la la')
    case '2':
        rez = 'Antradienis'
        print(f'Mes ivedeme {diena}')
        print('Tra la la')
    case '3':
        rez = 'Trečiadienis'
        print(f'Mes ivedeme {diena}')
        print('Tra la la')
    case '4':
        rez = 'Ketvirtadienis'
        print(f'Mes ivedeme {diena}')
        print('Tra la la')
    case '5':
        rez = 'Penktadienis'
        print(f'Mes ivedeme {diena}')
        print('Tra la la')
    case '6':
        rez = 'Seštadienis'
        print(f'Mes ivedeme {diena}')
        print('Tra la la')
    case '7':
        rez = 'Sekmadienis'
        print(f'Mes ivedeme {diena}')
        print('Tra la la')
    case _:
        rez = 'Blogai įvesti duomenys'

print(f'{diena} -----> {rez}')