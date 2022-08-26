
import sqlite3
from datetime import date


def lister(db):
    con = sqlite3.connect(
        "napoleon.sqlite3")
    cur = con.cursor()
    cur.execute("Select * from eleve")
    rows = cur.fetchall()
    for el in rows:
        print(
            el[0], "\t",
            el[1], "\t",
            el[2], "\t",
            el[3], "\t",
            el[4], "\t",
            el[5]
        )
    con.commit()
    con.close()


def rechercher(db):
    print("Vous avez choisi de rechercher")


def ajouter(db):

    con = sqlite3.connect("napoleon.sqlite3")
    cur = con.cursor()
    cur.execute("Select * from eleve")
    rows = cur.fetchall()

    matricule = input("Veuillez saisir la matricule de l'étudiant")
    nom = input("Veuillez saisir votre nom: ")
    prenom = input("Veuillez saisir votre prenom: ")
    anglais = float(input("Veuillez saisir les points obtenus en anglais: "))
    maths = float(input("Veuillez saisir les points obtenus en maths: "))

    annee = int(input("Saississez l'année de naissance"))
    mois = int(input("Saississez le mois de naissance"))
    jour = int(input("Saisissez le jour de naissance"))
    datenaissance = f"{annee}/{mois}/{jour}"

    print(f"Votre  date de naissance est:  {datenaissance}")

    cur.execute(f"""
            INSERT INTO eleve (nom, prenom, datenaissance, maths, anglais) 
            VALUES 
            ("{matricule} ","{nom} ", "{prenom}", {datenaissance}, {maths},{anglais} )
            """)
    con.commit()
    con.close()


def modifier(db):
    #print("Vous avez choisi de modifier")
    matricule = input("Veuillez saisir la matricule de l'étudiant: ")
    eleve = None
    index = -1
    for i, ele in enumerate(db):
        if ele["matricule"] == matricule:
            eleve = ele
            index = i

            break
    if index != -1:
        nom = input("Nouveau nom")
        prenom = input("Nouveau prenom")
        anglais = float(
            input("Veuillez saisir les nouveaux points obtenus en anglais: "))
        maths = float(
            input("Veuillez saisir les nouveaux points obtenus en maths: "))
        # eleve = {
        #     "no": no,
        #     "nom": nom if nom != " " else eleve["nom"],
        #     "prenom": prenom if prenom != "" else eleve[prenom],
        #     "anglais": anglais if anglais != "0.0" else eleve[anglais],
        #     "maths": maths if maths != "0.0" else eleve[maths],
        #     "annee": annee if annee != " " else eleve[annee],
        #     "mois": mois if mois != " " else eleve[mois],
        #     "jour": jour if jour != " " else eleve[jour]
        #     # "datenaissance" =  datenaissance if annee !="0 " or mois!="0 " or jour!=" 0" else eleve[datenaissance]
        # }

        db[index] = eleve
    else:
        print("L'eleve n'existe pas")


def supprimer(db):
    no = input(
        "Veuillez saisir votre matricule de l'élève que vous voulez supprimer: ")
    eleve = None
    index = -1
    for i, del_elv in enumerate(db):
        if del_elv["no"] == no:
            eleve = del_elv
            index = i
            break
    if index != -1:
        db.remove(eleve)
    else:
        print("L'eleve n'existe pas")

    #print("Vous avez choisi de supprimer")


#
# Quand on n'a pas encore créé la base de données
# from datetime import date


# def lister(db):
#     for el in db:
#         print(
#             el['no'], "\t",
#             el['nom'], "\t",
#             el['prenom'], "\t",
#             el['anglais'], "\t",
#             el['maths']
#         )


# def rechercher(db):
#     print("Vous avez choisi de rechercher")


# def ajouter(db):
#     #print("Vous avez choisi d'ajouter")
#     no = input("Veuillez saisir votre matricule: ")
#     nom = input("Veuillez saisir votre nom: ")
#     prenom = input("Veuillez saisir votre prenom: ")
#     anglais = float(input("Veuillez saisir les points obtenus en anglais: "))
#     maths = float(input("Veuillez saisir les points obtenus en maths: "))

#     annee = int(input("Saississez l'année de naissance"))
#     mois = int(input("Saississez le mois de naissance"))
#     jour = int(input("Saisissez le jour de naissance"))
#     datenaissance = annee+mois+jour

#     print(f"Votre  date de naissance est:  {annee}/{mois}/{jour}")

#     eleve = {
#         "no": no,
#         "nom": nom,
#         "prenom": prenom,
#         "anglais": anglais,
#         "maths": maths,
#         "annee": annee,
#         "mois": mois,
#         "jour": jour,
#         "datenaissance": datenaissance
#     }
#     db.append(eleve)


# def modifier(db):
#     #print("Vous avez choisi de modifier")
#     no = input("Veuillez saisir votre matricule: ")
#     eleve = None
#     index = -1
#     for i, ele in enumerate(db):
#         if ele["no"] == no:
#             eleve = ele
#             index = i

#             break
#     if index != -1:
#         nom = input("Nouveau nom")
#         prenom = input("Nouveau prenom")
#         anglais = float(
#             input("Veuillez saisir les nouveaux points obtenus en anglais: "))
#         maths = float(
#             input("Veuillez saisir les nouveaux points obtenus en maths: "))
#         eleve = {
#             "no": no,
#             "nom": nom if nom != " " else eleve["nom"],
#             "prenom": prenom if prenom != "" else eleve[prenom],
#             "anglais": anglais if anglais != "0.0" else eleve[anglais],
#             "maths": maths if maths != "0.0" else eleve[maths]
#         }

#         db[index] = eleve
#     else:
#         print("L'eleve n'existe pas")


# def supprimer(db):
#     no = input(
#         "Veuillez saisir votre matricule de l'élève que vous voulez supprimer: ")
#     eleve = None
#     index = -1
#     for i, del_elv in enumerate(db):
#         if del_elv["no"] == no:
#             eleve = del_elv
#             index = i
#             break
#     if index != -1:
#         db.remove(eleve)
#     else:
#         print("L'eleve n'existe pas")

#     #print("Vous avez choisi de supprimer")
