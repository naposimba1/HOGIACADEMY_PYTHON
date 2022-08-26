from eleve import Eleve


# jewe = Eleve("68", "simbandumwe", "M", "12.5", "15")
# print(type(jewe))  # <class eleve>
# print(jewe)  # No nom Sex, maths, anglais
# print(jewe.total())  # 27.5  donc anglais+ maths
# print(jewe.moyenne())  # 27.5/2


menu = """
Selectionner l'action:
    (1) Creer un eleve
    (2) Afficher les eleves
    (3) Modifier un eleve
    (4) Supprimer un eleve
    (5) Chercher un eleve
    (0) Quitter
     """
routes = {
    "1" fonctions.creer,
    "2" fonctions.afficher,
    "3" fonctions.modifier,
    "4" fonctions.supprimer,
    "5" fonctions.chercher
}
