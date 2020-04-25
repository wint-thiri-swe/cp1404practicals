"""
Github link : https://github.com/wint-thiri-swe/cp1404practicals/blob/master/prac04/list_exercises.py

CP 1404 Practical
Basic list operations and Woefully inadequate security checker
"""

# for loop that creates a new list containing the 5 numbers
number_list = []
for i in range(0, 5):
    numbers = int(input("Number: "))
    number_list.append(numbers)
print("The first number {}".format(number_list[0]))
print("The is the last number {}".format(number_list[4]))
print("The smallest number is {}".format(min(number_list)))
print("The largest number is {}".format(max(number_list)))
total = sum(number_list)
print("The average of the numbers is {}".format(total/len(number_list)))
# print output

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup',
             'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter username: ")  # ask user input
if username in usernames:  # check valid user
    print("Access granted")
else:
    print("Access denied")
    # print output
