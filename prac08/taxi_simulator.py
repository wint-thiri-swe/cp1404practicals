from prac08.taxi import Taxi
from prac08.silver_service_taxi import SilverServiceTaxi


def main():
    """Choose taxi to drive and print out total bills"""

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total = 0
    print("Let's drive!")
    menu_option = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    while menu_option != 'q':
        if menu_option == 'c':
            print("Taxis available:")
            show_taxi(taxis)
            choose_taxi = int(input("Choose taxi: "))
            chosen_taxi = taxis[choose_taxi]
        elif menu_option == 'd':
            chosen_taxi.start_fare()
            distance = float(input("Drive how far? "))
            chosen_taxi.drive(distance)
            drive_cost = chosen_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(chosen_taxi.name, drive_cost))
            total += drive_cost
        else:
            print("Invalid menu")
        print("Bill to date: ${:.2f}".format(total))
        menu_option = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    print("Total trip cost: ${:.2f}".format(total))
    print("Taxis are now: ")
    show_taxi(taxis)


def show_taxi(taxis):
    """Print available taxis with index at front"""
    for index, taxi in enumerate(taxis):
        print('{} - {}'.format(index, taxi))


if __name__ == '__main__':
    main()
