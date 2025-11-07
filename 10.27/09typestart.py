# == lygu
# != nelygu
# >  daugiau
# >= daugiau lygu
# <  maziau lygu
# <= maziau lygu
# in patikrina ar egzistuoja toks elementas

# and daugyba(logine)
# or sudetis(logine)
# not neigimas

# t1 = 5 == 2 FALSE
# t1 = 5 != 2 TRUE
# t1 = 5 > 5 FALSE
# t1 = 5 >= 5 TRUE
# t1 = 5 < 5 FALSE
t1 = 5 <= 5 #TRUE
print(t1)

t2 = 'a' in 'labas' #Ar raide a yra zodyje 'labas'
t2 = ('A' in 'labas') or ('a' in 'labas') #Ar raide a yra zodyje 'labas'
print(t2)