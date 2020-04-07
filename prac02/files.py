"""Files"""

def write():
    name = input("enter name")
    name_file = open("name.txt", "w")
    name_file.write(name)
    name_file.close()


def read():
    name_file = open("name.txt", "r")
    file_contents = name_file.read()
    name_file.close()
    print("Your name is ", file_contents)


def numbers():
    result = 0
    numbers_file = open("numbers.txt", "r")
    num1 = int(numbers_file.readline())
    num2 = int(numbers_file.readline())
    numbers_file.close()
    result += num1 + num2
    print(result)


def numbers1():
    numbers_file = open("numbers.txt", 'r')
    total = 0
    for lines in numbers_file:
        number = int(lines)
        total += number
    numbers_file.close()
    print(total)


def main():
    write()
    read()
    numbers()
    numbers1()


if __name__ == "__main__":
    main()
