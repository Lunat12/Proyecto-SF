
import random
from matplotlib import pyplot as plt
import datetime

def graf(listN):
    listD = []
    date = 0
    for n in listN:
        date += 1
        listD.append(date)
    print(listD)
    plt.plot(listD,listN)
    plt.show()
    


print('WELCOME TO THE BASIC TRADING BOT')

currencies = ['Bitcoin', 'Ada', 'Ethereum', 'Solana']

currency = input('Select a currency to work with: ').title()

try:
    money = float(input('How much money do you want to invest: '))
    H_resistance = float(input('Wheres the highest point you wanna be taking your money out (percentage): '))
    L_resistance = float(input('Wheres the lowest point you wanna be taking your money out (percentage):'))
except:
    print('You can only enter numbers.')

H_percent = money * (H_resistance / 100)
L_percent =  -money * (L_resistance / 100)

print(H_percent,' ', L_percent)

points = []

isActive = True
while isActive:
    num = random.randint(-50, 500)
    points.append(num)
    print(num)
    if num >= H_percent or num <= L_percent:
        isActive = False

graf(points)

