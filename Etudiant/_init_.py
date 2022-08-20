from fonctions import modifier, supprimer
from datetime import date, time, datetime
from fonctions import *
db = []

while True:
    choix = input(""""
                  Vous voulez: 
                  (1) Ajouter \n
                  (2) Modifier \n
                  (3) Supprimer \n
                  (4) Lister \n
                  (5) Rechercher \n
                  (0) pour terminer:"""

                  )
    if (choix == "1"):
        ajouter(db)
    elif (choix == "2"):
        modifier(db)
    elif (choix == "3"):
        supprimer(db)
    elif (choix == "4"):
        lister(db)
    elif (choix == "5"):
        rechercher(db)
    else:
        break

    # print("Vous a tapé", choix)
