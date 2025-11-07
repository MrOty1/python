def filmoPabaiga(val, min, trukmeVal, trukmeMin):
    visosMin = val * 60 + min + trukmeVal * 60 + trukmeMin
    pabaigosVal = visosMin // 60
    pabaigosMin = visosMin % 60
    return pabaigosVal, pabaigosMin



filmoPradziaVal = int(input("Kelintą valandą prasidėjo filmas?"))
filmoPradziaMin = int(input("Kurią minutę prasidėjo filmas?"))

filmoTrukmeVal = int(input("Kiek valandų trunko filmas?"))
filmoTrukmeMin = int(input("Kiek minučių trunko filmas?"))

filmoPabaigosVal, filmoPabaigosMin = filmoPabaiga(filmoPradziaVal, filmoPradziaMin, filmoTrukmeVal, filmoTrukmeMin)
print(f"Filmas baigsis: {filmoPabaigosVal:02d}:{filmoPabaigosMin:02d}")