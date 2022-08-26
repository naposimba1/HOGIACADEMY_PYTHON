from eleve import Eleve
from classes import Classe


def creer():
    no = input("Saisissez le no: ")
    fullname = input("Saisissez le nom: ")
    sexe = input("Saisissez le sexe: ")
    maths = input("Saisissez note maths: ")
    anglais = input("Saisissez note anglais: ")

    eleve = Eleve(no, fullname, sexe, maths, anglais)
    classes.ajouter(eleve)


# def afficher(classe):


def modifier(classe):
    no = input("Saisissez le no: ")
    fullname = input("Saisissez le nom: ")
    sexe = input("Saisissez le sexe: ")
    maths = input("Saisissez note maths: ")
    anglais = input("Saisissez note anglais: ")


def supprimer(classe):
    no = input("Saisissez le no: ")


def chercher(classe):
    no = input("Saisissez le no: ")
