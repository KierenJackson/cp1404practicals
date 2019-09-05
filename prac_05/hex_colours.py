COLOURS = {"RED": "#ff0000", "YELLOW": "#eedd82", "BLUE": "#0000cd", "PINK": "#ff34b3", "PURPLE": "	#8470ff",
           "GREEN": "#32cd32", "ORANGE": "#ffa500", "WHEAT": "#f5deb3", "WHITE": "#ffffff", "BLACK": "#0d0d0d"}

colour = input("Colour: ").upper()

while colour != "":
    if colour in COLOURS:
        print("{} is {}".format(colour.title(), COLOURS.get(colour, 0)))
    else:
        print("That is not a valid colour")
    colour = input("Colour: ").upper()

