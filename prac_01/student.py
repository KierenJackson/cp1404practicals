from prac_01.person import Person


class Student(Person):
    def __init__(self, name="", age=0, student_id=0):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return "{} is {} years old and their student id is {}".format(self.name, self.age, self.student_id)
