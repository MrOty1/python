vidurkis = float(input("Vidurkis = ")) #8.5
lankomumas = int(input("Lankomumas = ")) #80

if vidurkis >= 9 and lankomumas >= 90:
    print("Padidinta stipendija")
elif vidurkis >= 7 and lankomumas >= 75:
    print("Paprasta stipendija")
elif vidurkis < 7 or lankomumas < 60:
    print("stipendija neskiriama")
else:
    print("Reikia komisijos sprendimo")
