
"""
CP1404/CP5632 - Practical
Broken program to determine score status

Github link : https://github.com/wint-thiri-swe/cp1404practicals/blob/master/prac03/broken_score.py
"""
import random


def main():
    score = float(input("Enter score: "))
    final_score = check_score(score)
    print(final_score)
    print("Printing random score result...")
    score = random.randint(0, 120)  # random score
    random_score = check_score(score)
    print(random_score)


def check_score(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


if __name__ == "__main__":
    main()
