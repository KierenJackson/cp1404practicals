#OUTPUT_FILE = "name.txt"
NUMBERS_FILE = "numbers.txt"

#out_file = open(OUTPUT_FILE, 'w')

#name = input("Please enter your name: ").title()
#print(name, file=out_file)

#out_file.close()

#out_file = open(OUTPUT_FILE, 'r')

#print("Your name is {}".format(out_file.read()))

#out_file.close()

number_file = open(NUMBERS_FILE, 'r')

numbers = number_file.readlines()

print(numbers)

summed = 0
for i in range(len(numbers)):
    summed = summed + int(numbers[i])
print(summed)

number_file.close()
