tOneMin = int(input('How many MINUTES did it take to run TRACK ONE: '))
tOneSec = int(input('How many SECONDS did it take to run TRACK ONE: '))
tTwoMin = int(input('How many MINUTES did it take to run TRACK TWO: '))
tTwoSec = int(input('How many SECONDS did it take to run TRACK TWO: '))

totalMins = tOneMin + tTwoMin
totalSecs = tOneSec + tTwoSec
totalMins += totalSecs // 60
totalSecs = totalSecs % 60

if totalMins > 0:
    print(f'It takes {totalMins} minutes and {totalSecs} seconds, to run both tracks')
else:
    print(f'It takes {totalSecs} seconds, to run both tracks')