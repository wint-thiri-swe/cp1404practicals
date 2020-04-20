"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    print("----------")
    print_subject_details()


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    file_list = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked

        print("----------")
        file_list.append(parts)  # add parts to the empty list
    input_file.close()
    return file_list    # return the list to variable


def print_subject_details():
    """ Print subject details from the txt file with string format"""
    input_file = open(FILENAME).read().splitlines()
    for line in input_file:
        parts = line.split(',')
        print("{} is taught by {} and has {} students".format(parts[0], parts[1], parts[2]))


if __name__ == '__main__':
    main()
