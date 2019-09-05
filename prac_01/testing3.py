class User:

    def __init__(self, name=""):
        self.name = name
        self.number_of_tacos = 5
        self.score = 0

    def give_taco(self, other):
        if self.number_of_tacos > 0:
            self.number_of_tacos -= 1
            other += 1
            self.score += 1
            return other
        else:
            print("Not enough tacos to give out")

    def __str__(self):
        return "{}, {} points, {} tacos left".format(self.name, self.score, self.number_of_tacos)


user1 = User("Kieren")
user2 = User("Dom")


print(user1.number_of_tacos)
print(user2)
