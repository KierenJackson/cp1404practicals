from prac_06.guitar import Guitars

guitar1 = Guitars("Epic Guitar", 1922, 16035.40)

guitar1_age = guitar1.get_age()

print(guitar1_age)

if guitar1.is_vintage(guitar1_age):
    print("Is vintage")

