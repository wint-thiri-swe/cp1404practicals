"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


CODE_TO_NAME = {"QLD": "Queensland",
                "NSW": "New South Wales",
                "NT": "Northern Territory",
                "WA": "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria",
                "TAS": "Tasmania"}

print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()   # accept lower case input
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()  # accept lower case input

for state_code in CODE_TO_NAME:  #
    print("{:4} is {:4}".format(state_code, CODE_TO_NAME[state_code]))  # for loop to print neatly
