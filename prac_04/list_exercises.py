numbers = []

for number in range(1, 6):
    numbers.append(int(input("Please enter a number: ")))

sum_of_numbers = sum(numbers)
average = sum_of_numbers/5

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The lowest number is {}".format(min(numbers)))
print("The highest number is {}".format(max(numbers)))
print("The sum of the numbers is {}".format(sum_of_numbers))
print("The average of the numbers is {}".format(average))

