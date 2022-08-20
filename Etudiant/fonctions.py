def lister(db):
    for el in db:
        print(
            el['no'], "\t",
            el['nom'], "\t",
            el['prenom'], "\t",
            el['anglais'], "\t",
            el['maths']
        )


def rechercher(db):
    print("Vous avez choisi de rechercher")


def ajouter(db):
    #print("Vous avez choisi d'ajouter")
    no = input("Veuillez saisir votre matricule: ")
    nom = input("Veuillez saisir votre nom: ")
    prenom = input("Veuillez saisir votre prenom: ")
    anglais = float(input("Veuillez saisir les points obtenus en anglais: "))
    maths = float(input("Veuillez saisir les points obtenus en maths: "))

    eleve = {
        "no": no,
        "nom": nom,
        "prenom": prenom,
        "anglais": anglais,
        "maths": maths
    }
    db.append(eleve)


def modifier(db):
    #print("Vous avez choisi de modifier")
    no = input("Veuillez saisir votre matricule: ")
    eleve = None
    index = -1
    for i, ele in enumerate(db):
        if ele["no"] == no:
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
        eleve = {
            "no": no,
            "nom": nom if nom != " " else eleve["nom"],
            "prenom": prenom if prenom != "" else eleve[prenom],
            "anglais": anglais if anglais != "0.0" else eleve[anglais],
            "maths": maths if maths != "0.0" else eleve[maths]
        }

        db[index] = eleve
    else:
        print("L'eleve n'existe pas")


def supprimer(db):
    print("Vous avez choisi de supprimer")
