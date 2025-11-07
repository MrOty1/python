# 154cnt = 1 Eur 54 cnt

money = float(input('How many cents do you have: '))
if money // 100:
    eur = money // 100
else:
    eur = 0
cent = money % 100
print(f'You have {eur} EUR and {cent} cents')