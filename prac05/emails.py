"""
Github link: https://github.com/wint-thiri-swe/cp1404practicals/blob/master/prac05/emails.py

CP1404/CP5632 Practical
Emails and names in a dictionary
File needs reformatting
"""


emails_to_name = {}     # creates empty dictionary


def get_name_from_email(email):
    font_name = email.split('@')[0]     # split '@' part from email
    dot_part = font_name.split('.')     # split '.' part from email
    name = ' '.join(dot_part).title()   # join the previous split
    return name


def main():
    # ask user email input
    email = input("Email: ")
    while email != ' ':
        name = get_name_from_email(email)
        print("Is your name {}".format(name.title()))   # check valid name
        check_name = input("Y/n").lower()
        if check_name == 'n':
            name = input("Name:")
            emails_to_name[email] = name    # add name to dictionary
        else:
            emails_to_name[email] = name
        email = input("Email: ")

    # for loop to print name and email
    for email, name in emails_to_name.items():
        print('{} ({})'.format(name.title(), email))


if __name__ == '__main__':
    main()
