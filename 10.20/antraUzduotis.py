carDistance = int(input('How many Kilometers are you driving: ')) #100KM
carUsage = int(input('How many liters does your car use per 100km: ')) #8KM
gasPrice = float(input('How much does gas cost per 1 liter: '))
carPeople = int(input('How many people are in the car: '))

carDistanceGas = (carDistance * carUsage) / 100
gasPriceTotal = gasPrice * carDistanceGas
gasPricePeople = gasPriceTotal / carPeople

print(f'Total gas price is: {round(gasPriceTotal, 2)}EUR, each person has to pay {round(gasPricePeople, 2)}EUR')