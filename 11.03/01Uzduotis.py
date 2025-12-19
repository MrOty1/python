t1 = int(input("T1 = ")) #9 
t2 = int(input("T2 = ")) #7 
t3 = int(input("T3 = ")) #8 
t4 = int(input("T4 = ")) #10 

maz = t1
#randamas maziausias skaicius
if t2 < maz:
    maz = t2
if t3 < maz:
    maz = t3
if t4 < maz:
    maz = t4

did = t1
#randamas didziausias skaicius
if t2 > did:
    did = t2
if t3 > did:
    did = t3
if t4 > did:
    did = t4

suma = t1 + t2 + t3 + t4
likusiSuma = suma - maz - did #pasalina min ir did
vidurkis = likusiSuma / 2
print(f"Teiseju balas {vidurkis}")

