leistinasGreitis = int(input("Leistinas greitis = ")) #50
vairuotojoGreitis = int(input("Savo greiti = ")) #82

KiekVirsyta = vairuotojoGreitis - leistinasGreitis

if KiekVirsyta <= 0:
    print("Nevirsytas")
elif KiekVirsyta >= 1 and KiekVirsyta <= 10:
    print(f"Virsyta {KiekVirsyta} km/h - ispejimas")
elif KiekVirsyta >= 11 and KiekVirsyta <= 30:
    print(f"Virsyta {KiekVirsyta} km/h - Bauda 30$")
elif KiekVirsyta >= 31 and KiekVirsyta <= 50:
    print(f"Virsyta {KiekVirsyta} km/h - Bauda 100$")
elif KiekVirsyta > 50:
    print(f"Virsyta {KiekVirsyta} km/h - Bauda 300$ + pazymejimo atemimas")