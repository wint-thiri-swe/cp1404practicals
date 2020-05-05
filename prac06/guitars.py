"""
Github link: https://github.com/wint-thiri-swe/cp1404practicals/blob/master/prac06/guitars.py
"""


from prac06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")

    # ask for user input
    name = input("Name: ")
    while name != " ":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print("{} ({}) : ${} added.".format(name, year, cost))
        guitars.append(Guitar(name, year, cost))    # add to list
        name = input("Name: ")
    print("There are my guitars:")

    # for loop to print each elements in list
    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():  # called the method from guitar class
            vintage_string = "(vintage)"
            print("Guitar {}: {} ({}), worth ${:3,.2f} {}".format(i + 1, guitar.name, guitar.year,
                                                                  guitar.cost, vintage_string))
        else:
            print("Guitar {}: {} ({}), worth ${:3,.2f}".format(i + 1, guitar.name, guitar.year,
                                                               guitar.cost))


if __name__ == '__main__':
    main()
