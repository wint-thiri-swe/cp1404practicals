"""Program to display all odd numbers between 1 and 20
with a space between each one."""


def main():
    for i in range(1, 21, 2):
        print(i, end=" ")
    print()


main()

"""a. count in 10s from 0 to 100"""


def loopsa():
    for i in range(0, 110, 10):
        print(i, end=" ")
    print()


loopsa()

"""b. count down from 20 to 1"""


def loopsb():
    for i in range(20, 0, -1):
        print(i, end=" ")
    print()


loopsb()

"""c. print n stars"""


def starloop():
    number_of_star = int(input("Enter number"))
    for i in range(0, number_of_star):
        print("*", end="")
    print()


starloop()

"""d. print n lines of increasing stars"""


def increasingstar():
    number_of_star = int(input("Enter number"))
    for i in range(0, number_of_star, 1):
        for j in range(0, i + 1):
            print("*", end="")
        print()


increasingstar()
