# Petriuko pazymiai
kiek = int(input("Kiek pazymiu: "))
sar = []

kelintas = 0
while kelintas < kiek:
    paz = int(input(f'Koks {kelintas+1}-asis pazymys: '))
    if 1<=paz<=10:
        sar.append(paz)
        kelintas += 1
    else:
        print(f'{paz} netinkamas')
print(sar)