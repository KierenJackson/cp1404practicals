"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():

    score = float(input())
    result = calculate_grade(score)
    print(result)


def calculate_grade(grade):
    if grade < 0 or grade > 100:
        result = "Invalid score"
    elif grade >= 90:
        result = "Excellent"
    elif grade >= 50:
        result = "Pass"
    elif grade < 50:
        result = "Bad"
    return result


main()

