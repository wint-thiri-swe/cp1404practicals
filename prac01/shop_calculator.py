"""A program to calculate the total price after discount"""


def main():
    total_price = 0
    num_of_items = int(input("Number of items: "))
    while num_of_items < 0:
        print("Invalid number of items!")
        num_of_items = int(input("Number of items: "))
    for i in range(0, num_of_items, 1):
        price_of_item = float(input("Price of item: "))
        total_price += price_of_item
    if total_price > 100:
        total_price -= total_price * 0.1
    print("Total price for {} items is ${:.2f}".format(num_of_items, total_price))


if __name__ == "__main__":
    main()
