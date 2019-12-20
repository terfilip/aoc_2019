import os
import pyperclip

with open('1.txt', 'r') as f:
    masses = [int(line) for line in f.readlines()]

total_fuel = sum((mass // 3 - 2 for mass in masses))

print(f'1.1: {total_fuel}')

def get_fuel(mass):

    cfuel = mass // 3 - 2
    tfuel = cfuel

    while cfuel > 0:
        cfuel = cfuel // 3 - 2
        tfuel += max(cfuel, 0)
    
    return tfuel

total_fuel_v2 = sum((get_fuel(mass) for mass in masses))
pyperclip.copy(total_fuel_v2)
print(f'1.2: {total_fuel_v2}')
