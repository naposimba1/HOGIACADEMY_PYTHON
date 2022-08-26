from mimetypes import init
from select import select


from eleve import Eleve


class Classe:
    def __init__(self, nom):
        self.nom = nom
        self.eleves: list[Eleve] = []

    def rechercher(self, id):
        for e in self.eleves:
            if e.no == id:
                return e
        return None

    def ajouter(self, eleve):
        eleve = self.rechercher(eleve, no)
        if (eleve):
            raise Exception("L'élève existe déjà")
        else:
            self.eleves.append(eleve)

    def supprimer(self, id):
        eleve = self.rechercher(id)
        if (eleve):
            self.eleve.remove(eleve)

    def __str__(self):
        for e in self.eleves:
            print(f"{e.no } {e.fullname} {e.sexe} {e.maths} {e.anglais} ")

        # e.no = no
        # e.fullname = fullname
        # e.sexe = sexe
        # e.maths = maths
        # e.anglais = anglais

#list [start:end]
