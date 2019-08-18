for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_times = int(input("How many n stars: "))

for i in range(number_of_times):
    print("*", end=" ")

for i in range(number_of_times + 1):
    print('*' * i)
print()
