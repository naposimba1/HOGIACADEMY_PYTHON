
a = str("napoLeon")
# type(a)

# a.capitalize()
# a.upper()

# a.split()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher(self):
        print(self.x, self.y)

    def __str__(self):
        return ("Point({}, {})"
                format(self.x, self.y))


b = Point(4, 12)
b.afficher()
