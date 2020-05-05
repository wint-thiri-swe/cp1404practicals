from prac06.guitar import Guitar


def main():
    """Demo code to test out Guitar class"""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(guitar1)
    print(guitar1.get_age())
    print(guitar1.is_vintage())

    guitar2 = Guitar("Gibson L-5 CES", 2013, 16035.40)
    print(guitar2)
    print(guitar2.get_age())
    print(guitar2.is_vintage())


if __name__ == '__main__':
    main()
