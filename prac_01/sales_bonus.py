"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("How much was the sale: "))
while sales < 0:
    print("That's a negative number!")
    sales = float(input("How much was the sale: "))
if sales < 1000:
    bonus = sales * 0.1
    print("You will receive a $" + str(bonus), "bonus!")
else:
    bonus = sales * 0.15
    print("You will receive a $" + str(bonus), "bonus!")

