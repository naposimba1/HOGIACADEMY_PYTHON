class Point:
    def __init__(this, x, y):
        this.x = x
        this.y = y

    def __str__(this):
        return f"{this.x}, {this.y}"

    def add(this, point):
        return Point(this.x + point.x, this.y + point.y)

        # x_new = this.x+point.x
        # y_new = this.y+point.y
        # return Point(x_new, y_new)

    def times(this, nombre):
        x_new = this.x*nombre
        y_new = this.y*nombre
        return Point(x_new, y_new)


a = Point(1, 1)
b = Point(2, 2)

print(a, b)
print(a.add(b))
print(a.times(2))
