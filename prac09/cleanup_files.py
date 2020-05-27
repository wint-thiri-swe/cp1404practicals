"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 2: move file to new place, with new name
        shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", '_').replace(".TXT", '.txt')
    new_name = ""
    for current_index, current_character in enumerate(filename):
        previous_character = filename[current_index - 1]

        if previous_character == '_' and current_character.isalnum():
            current_character = current_character.upper()
        new_name = new_name + current_character

        if current_index < len(filename) - 1:
            next_character = filename[current_index + 1]

            if current_character.isalnum() and (next_character.isupper() or next_character.isdigit()):
                new_name += '_'
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # for loop to rename files
        for filename in filenames:
            fullname = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            print("Renaming {} to {}".format(filename, new_name))
            os.rename(fullname, new_name)


main()
# demo_walk()