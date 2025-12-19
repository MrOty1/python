suma = float(input("Ivesk saskaitos suma: ")) #65
lojalumoKortele = input("Ar turite lojalumo kortele?  ") #ne

if suma > 100:
    nuolaida = 0.15
elif suma >= 50 and suma <= 100:
    nuolaida = 0.10
elif suma <= 50 and lojalumoKortele == "taip":
    nuolaida = 0.05
else:
    nuolaida = 0

galutineSuma = suma - (suma * nuolaida)

if nuolaida > 0:
    print(f"nuolaida: {nuolaida * 100}% - moketi {galutineSuma}$")
else:
    print(f"Be nuolaidos: moketi {galutineSuma}$")
