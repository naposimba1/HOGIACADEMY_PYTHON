class Personne:
    def __init__(self, nom="sans", prenom="sans"):
        self.nom = nom
        self.prenom = prenom
        self.residence = "Bujumbura"

    def __str__(self):
        return "Izina ryanje ni {} bantazira {} mba {} ".\
            format(self.nom, self.prenom, self.residence)

    def kwimuka(self, lieu):
        self.residence = lieu


class Etudiant(Personne):
    def __init__(self, nom, prenom, matr=000):
        Personne.__init__(self, nom, prenom)
        self.matr = matr

    def __str__(self):
        return "Izina ryanje ni {} bantazira {} mba {} matricule {} ".\
            format(self.nom, self.prenom, self.residence, self.matr)
