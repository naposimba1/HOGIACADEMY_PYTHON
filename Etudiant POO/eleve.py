from ast import MatchSequence


class Eleve:
    def __init__(self, no, fullname, sexe, maths, anglais):
        self.no = no
        self.fullname = fullname
        self.sexe = sexe
        self.maths = maths
        self.anglais = anglais

    def total(self):
        return self.anglais + self.maths

    def moyenne(self):
        return self.total()/2

    def __str__(self):
        return f"No.{self.no} {self.fullname}"
