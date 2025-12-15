def doCalc(one, two, three, four):
    gasUsage = one / 100
    gasDistance = gasUsage * two
    gasPrice = gasDistance * four
    personSplit = gasPrice / three
    print(f'kai k = {one},m = {two}, n = {three}, kk = {four}, tai s = {round(personSplit, 2)}')
    

k = 7.5
m = 305.5
n = 4
kk = 1.65

doCalc(k, m, n, kk)