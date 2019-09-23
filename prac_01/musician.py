from prac_01.person import Person


class Musician(Person):
    def __init__(self, name="", age=0, play_text=""):
        super().__init__(name, age)
        self.play_text = play_text

    def play_song(self):
        print(self.play_text)

    def __str__(self):
        return "{} is {} years old and the song they want to play is {}".format(self.name, self.age, self.play_text)

