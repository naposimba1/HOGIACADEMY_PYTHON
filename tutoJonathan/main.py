# def register():
#     print("--- Register ---")
#     username = input("Username : ")
#     password = input("Mot de passe : ")


# def menu_not_connected():
#     while True:
#         print("Bienvenue sur notre application ! (non connecté")
#         print("Choisissez une option")
#         print("1. Login")
#         print("2. S'inscrire")
#         choix = int(input())

#         if choix == 2:
#             register()


# menu_not_connected()

def afficher_info_personne(nom):
    # print("La personne est " toto + ", son age est", age, "ans")
    print("Le nom comporte", len(nom), "caractères")

    afficher_info_personne("Emile")
