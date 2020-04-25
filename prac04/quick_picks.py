"""
Github link : https://github.com/wint-thiri-swe/cp1404practicals/blob/master/prac04/quick_picks.py

CP 1404 Practical
"Quick Pick" Lottery Ticket Generator
"""
import random

NUMBER_PER_LINE = 6
MIN = 1
MAX = 45

number_of_lines = int(input("How many quick picks? "))
while number_of_lines < 0:
    print("Invalid number of quick picks")
    number_of_lines = int(input("How many quick picks? "))

# for loop to create 6 random numbers of lines based on user input
for i in range(number_of_lines):
    quick_pick = []
    for j in range(NUMBER_PER_LINE):
        number = random.randint(MIN, MAX)
        while number in quick_pick:
            number = random.randint(MIN, MAX)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join("{:3}".format(number) for number in quick_pick))
