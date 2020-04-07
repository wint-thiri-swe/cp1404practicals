"""Github link : """

"""Print stars by the number of characters in password"""

MIN_LENGTH = 6


def main():
    password = get_password()
    print_asterisk(password)


def print_asterisk(password):
    print("*" * len(password))


def get_password():
    password = input(">")
    while len(password) < MIN_LENGTH:
        print("invalid password, password should be at least 6 character")
        password = input(">")
    return password


main()
