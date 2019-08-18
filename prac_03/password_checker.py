MIN_LENGTH = 6


def main():
    print_password = ""
    password = get_password()

    print_password = asterisks_converter(password, print_password)

    print(print_password)


def asterisks_converter(password, print_password):
    for char in range(len(password)):
        print_password += "*"
    return print_password


def get_password():
    password = input("Please enter your password: ")
    while len(password) < MIN_LENGTH:
        print("Password must at least be {} characters long".format(MIN_LENGTH))
        password = input("Please enter your password: ")
    return password


main()

