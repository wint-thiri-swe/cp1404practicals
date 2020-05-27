"""
Sort files based on extension
"""
import os


def main():
    """Move files into folders with the same name as their extension."""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension_name = filename.split('.')[-1]
        try:
            os.mkdir(extension_name)
        except FileExistsError:
            pass
        print("{}/{}".format(extension_name, filename))
        os.rename(filename, "{}/{}".format(extension_name, filename))


main()