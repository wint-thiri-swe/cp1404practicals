from prac08.silver_service_taxi import SilverServiceTaxi


def main():
    # Create a new silver_service_taxi with the name 'Silver Taxi', 200 units of fuel, fanciness of 2
    silver_service_taxi = SilverServiceTaxi("Silver Taxi", 200, 2)

    # Drive the taxi 18 km
    silver_service_taxi.drive(18)

    # Print the taxi's details and current fare
    print(silver_service_taxi)
    print("Fare: ${:.2f}".format(silver_service_taxi.get_fare()))


if __name__ == '__main__':
    main()
