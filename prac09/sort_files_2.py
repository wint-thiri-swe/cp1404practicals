"""
Sort files based on extension and user categorisation
"""
import os


def main():
    """Move files into where user wants to store them based on extension."""
    extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension_name = filename.split('.')[-1]
        if extension_name not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension_name))
            extension_to_category[extension_name] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(extension_to_category[extension_name], filename))


main()