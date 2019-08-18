def main():
    age = 0
    finished = False

    while not finished:
        try:
            age = int(input("What is your age? "))
            if age < 1 or age > 100:
                print("Age must be between 1 and 100")
            else:
                finished = True
        except ValueError:
            print("Please enter a valid integer.")

    if is_even(age):
        print("Your age is even")
    else:
        print("Your age is odd")


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


main()
