from prac06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    language_list = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")

    # for loop to only print dynamically typed languages
    for language in language_list:
        if language.is_dynamic():  # called the method from class
            print(language.name)


if __name__ == '__main__':
    main()
