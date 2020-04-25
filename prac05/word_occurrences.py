"""
CP1404/CP5632 Practical
Words in a dictionary
Counting word occurrences
"""

words_to_count = {}  # empty dictionary


def count_occurrences(words):
    # for loop to count the number of occurrence
    for word in words:
        if word in words_to_count:
            words_to_count[word] += 1
        else:
            words_to_count[word] = 1


def main():
    words = input("Text: ").split()  # ask for user input
    words.sort()                    # sort user input
    count_occurrences(words)        # count occurrence function
    print_occurrence_value()        # print occurrence value of each word


def print_occurrence_value():
    max_key_length = max([len(key) for key in words_to_count.keys()])   # align the outputs in one nice column
    # for loop to print occurrence value
    for word, count in words_to_count.items():
        print("{:{col_width}} : {}".format(word, count, col_width=max_key_length))


if __name__ == '__main__':
    main()
