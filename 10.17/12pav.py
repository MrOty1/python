# Ivedamas pradzios laikas, ir ivedama darbo trukme min
# Apskaiciuoti kada mes baigem darba

prVal = int(input('Which hour did you start work: '))
prMin = int(input('Which minute did you start work: '))
trMin = int(input('How long did it take: '))
minCalc = prVal*60 + prMin + trMin
pbVal = minCalc // 60
pbMin = minCalc % 60
print(f'Work ends at {pbVal}:{pbMin}')