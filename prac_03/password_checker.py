MIN_LENGTH = 6


def main():
    print_password = ""
    password = input("Please enter your password: ")
    while len(password) < MIN_LENGTH:
        print("Password must at least be {} characters long".format(MIN_LENGTH))
        password = input("Please enter your password: ")

    for char in range(len(password)):
        print_password += "*"

    print(print_password)


main()

