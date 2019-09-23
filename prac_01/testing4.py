from prac_01.musician import Musician
from prac_01.student import Student

bob = Student("Bob", 18, 18235876)
sally = Musician("Sally", 18, "The wind is you")

sally.play_song()
print(sally)
print(bob)