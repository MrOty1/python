def doClock(min1, min2, sec1, sec2):
    visosSec = (sec1 + sec2) % 60
    visosMin = min1 + min2 + (sec1 + sec2) // 60
    print(f'Petriukas užtruko {visosMin}min. ir {visosSec}sek.')

x1 = 1
y1 = 45
x2 = 2
y2 = 20

doClock(x1, x2, y1, y2)