MT = int(input("Matematika = ")) #8 
LT = int(input("Lietuviu = ")) #9
IT = int(input("Informacines technologijos = ")) #10

vidurkis = (MT + LT + IT) / 3 

if MT < 4 or LT < 4 or IT < 4:
    ivertinimas = "Neislaikyta" #jei bent vienas maziau 4
elif vidurkis >= 9:
    ivertinimas = "Puikiai"
elif vidurkis >= 7:
    ivertinimas = "Gerai"
else:
    ivertinimas = "Patenkinamai"

print(f"Vidurkis = {vidurkis} - {ivertinimas}")