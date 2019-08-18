import string


def main():
    string1 = "AbcD3h@1gd"
    print(count_letter(string1))


def count_letter(a_str):
    count = 0
    for char in a_str:
        if char.lower() in string.ascii_lowercase:
            count += 1
    return count


main()
