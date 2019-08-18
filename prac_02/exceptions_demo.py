"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When a value that isn't a number is entered
2. When will a ZeroDivisionError occur? When the user types a 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes
"""
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

while numerator == 0 or denominator == 0:
    print("Number must not be 0")
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
try:
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
