#suprogramuoti skaiciuotuva +, -, *, /
sk1 = int(input('Skaičius 1: '))
op = input('Pasirinkimas nborima operacija (+, -, *, /): ')
sk2 = int(input('Skaičius 2: '))

match op:
    case '+':
        rez = sk1 + sk2
        print(f'{sk1} + {sk2} = {rez}')
    case '-':
        rez = sk1 - sk2
        print(f'{sk1} - {sk2} = {rez}')
    case '*':
        rez = sk1 * sk2
        print(f'{sk1} * {sk2} = {rez}')
    case '/':
        match sk2:
            case 0:
                print('Dalyka iš nulio negalima')
            case _:
                rez = sk1 / sk2
                print(f'{sk1} / {sk2} = {rez}')
    case _:
        print(f'Pasirinkta operacija {op} negalima')