money = 100
goodbye = 0

def output(money):
    print('---Bankomatas---\n'
        '1. Parodyti likutį\n'
        '2. Įnešti pinigų\n'
        '3. Išsiimti pinigų\n'
        '4. Baigti')
    choice = int(input('Jūsų pasirinkimas: '))
    choiceOpt(choice, money)

def choiceOpt(chc, mny):
    if chc == 1:
        print(f'Likutis: {mny}$')
    elif chc == 2:
        add = int(input('Kiek įnešti: '))
        mny += add
    elif chc == 3:
        remove = int(input('Kiek išsiimti: '))
        if(remove > mny):
            print(f'truksta {(remove - mny)}$')
        else:
            mny -= remove
    elif chc == 4:
        goodbye += 1
        print(f'Viso Gero')
    else:
        print('BAD NUMBER')

while goodbye == 0:
    print(f'SSSSSSSSSSSSSSSSSSSSSS {goodbye}')
    if goodbye == 0:
        output(money)
    else:
        print('DISABLE@!!!!!!!!!!!')


# ADD RETURN AND FIX CODE