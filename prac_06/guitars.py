from prac_06.guitar import Guitars

guitars = []
amount_of_guitars = 0

# name = input("name:")
#
# while name != "":
#     year = int(input("Year: "))
#     cost = int(input("Cost: "))
#     guitars.append(Guitars(name, year, cost))
#     name = input("name:")

guitars.append(Guitars("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitars("Line 6 JTV-59", 2010, 1512.9))

print("These are my guitars!")


for guitar in guitars:
    amount_of_guitars += 1
    print("Guitar {}: {} ({}), worth $ {}".format(amount_of_guitars, guitar.name, guitar.year, guitar.cost))

