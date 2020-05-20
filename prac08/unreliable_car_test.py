from prac08.unreliable_car import UnreliableCar


def main():
    """Unreliable Car Test"""

    # Create cars with 2 different reliabilities
    first_car = UnreliableCar("Lambo", 200, 44)
    first_car.drive(100)
    print(first_car)

    second_car = UnreliableCar("Palisade", 200, 12)
    second_car.drive(100)
    print(second_car)


if __name__ == '__main__':
    main()
