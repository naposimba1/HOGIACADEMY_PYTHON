from re import X
from tkinter import Y


class Point:
    def __init__(self):
        self.x = X
        self.y = Y

    def afficher(self):
        print("Point({}, {})".format(self.x, self.y))

    def __add__(self, k):
        self.x += k
        self.y += k
