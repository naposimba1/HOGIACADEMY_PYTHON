from classe import Classe
import fonctions

menu = """
Selectionner une action:
(1) Creer un eleve
(2) Lister les eleves
(3) Modifier un eleve
(4) Supprimer un eleve
(5) Chercher un eleve
(0) Quitter:"""

routes = {
    "1": fonctions.creer,
    "2": fonctions.lister,
    "3": fonctions.modifier,
    "4": fonctions.supprimer,
    "5": fonctions.chercher,
}

classe = Classe("HOGI SCHOOL OF CODE")

while True:
    choix = input(menu)
    if (choix == '0'):
        break
    routes[choix](classe)
