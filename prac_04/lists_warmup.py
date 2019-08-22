numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0] = "ten"
numbers[-1] = 1
new_numbers = numbers[2:]
if 9 in numbers:
    print("9 is in numbers")
else:
    print("9 is not in numbers")

print(new_numbers)
