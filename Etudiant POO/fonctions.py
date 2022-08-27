from eleve import Eleve
from classe import Classe


def creer(classe):
    no = input("saisissez le no:")
    fullname = input("saisissez le fullname:")
    maths = input("saisissez les points maths:")
    engl = input("saisissez les points engl:")
    sexe = input("saisissez le sexe:")

    eleve = Eleve(no, fullname, maths, engl, sexe)
    try:
        classe.ajouter(eleve)
    except Exception as e:
        print("HABAYE IKIBAZO:", e)


def lister(classe):
    print(classe)


def modifier(classe):
    no = input("saisissez le no:")
    eleve = classe.rechercher(no)
    if (eleve):
        fullname = input("saisissez le fullname:")
        maths = input("saisissez les points maths:")
        engl = input("saisissez les points engl:")
        sexe = input("saisissez le sexe:")
        eleve.fullname = fullname
        eleve.maths = maths
        eleve.engl = engl
        eleve.sexe = sexe
    else:
        print("eleve introuvable")


def supprimer(classe):
    no = input("saisissez le no:")
    classe.supprimer(no)


def chercher(classe):
    no = input("saisissez le no:")
    eleve = classe.rechercher(no)
    if (eleve):
        print(eleve)
    else:
        print("eleve introuvable")
