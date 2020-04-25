"""
Github link: https://github.com/wint-thiri-swe/cp1404practicals/blob/master/prac05/hex_colours.py

CP1404/CP5632 Practical
Look up hexadecimal color codes
"""

COLOR_TO_CODE = {'gold1': '#ffd700',
                 'lightblue': '#add8e6',
                 'plum': '#dda0dd',
                 'powderblue': '#b0e0e6',
                 'hotpink': '#ff69b4',
                 'coral': '#ff7ff50',
                 'beige': "#f5f5dc",
                 'black': '#000000',
                 'chocolate': '#d2691e',
                 'dark khaki': '#bdb76b'}


def print_colors():
    for color, code in COLOR_TO_CODE.items():
        print("{:10} - {}".format(color, code))


def main():
    # ask user for input
    print_colors()
    color_name = input("Enter color: ").lower()
    while color_name != " ":
        print('Color code for {} is {}'.format(COLOR_TO_CODE.get(color_name), color_name))
        color_name = input("Enter color: ").lower()
    # print output as hexadecimal


if __name__ == '__main__':
    main()
