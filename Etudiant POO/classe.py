from eleve import Eleve


class Classe:
    def __init__(self, nom):
        self.nom = nom
        self.eleves: list[Eleve] = []

    def ajouter(self, eleve):
        found = self.rechercher(eleve.no)
        if (found):
            raise Exception(f"l'eleve No.{found.no} existe déjà")
        self.eleves.append(eleve)

    def rechercher(self, id):
        for eleve in self.eleves:
            if eleve.no == id:
                return eleve
        return None

    def supprimer(self, id):
        eleve = self.rechercher(id)
        if (eleve):
            self.eleves.remove(eleve)
        else:
            print("eleve introuvable")

    def __str__(self):
        string = f"VOICI LES ELEVES DE {self.nom}\n"
        for e in self.eleves:
            string += f"{e.no} {e.fullname} {e.maths} {e.engl} {e.sexe}\n"
        return string
