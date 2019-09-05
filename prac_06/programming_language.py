class ProgrammingLanguage:
    def __init__(self, field="", typing="", reflection="", year=0):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing.upper() == "DYNAMIC":
            return True
        elif self.typing.upper() == "STATIC":
            return False
        else:
            print("Wrong spelling")

    def __str__(self):

        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.field, self.typing, self.reflection, self.year)

