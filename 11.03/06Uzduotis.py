# 4 4 5 5 
# 3 10 10 3 
# 11 3 3 10 
a = int(input("Ivesk krastine a = ")) 
b = int(input("Ivesk krastine b = ")) 
c = int(input("Ivesk krastine c = ")) 
d = int(input("Ivesk krastine d = ")) 
#patikrina ar priesingos krastines lygios
if (a == c and b == d) or (a == b and c == d) or (a == d and b == c):
    print("Kurmiui zemes sklypo ribas pazymeti pavyks")
else:
    print("Kurmiui zemes sklypo ribas pazymeti nepavyks")