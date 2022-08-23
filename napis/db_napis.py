import sqlite3
from datetime import date, timedelta

umusi = date.today() + timedelta(days=30)
# pour se connecter à la BD nommée napoleon
con = sqlite3.connect("napoleon.sqlite3")

cur = con.cursor()

# si la BD n'existe pas, elle se crée directement

cur.execute(f"""
            INSERT INTO Salle (nom_preno, fete, nb_jour, date, montant) 
            VALUES 
            ("SIMBANDUMWE Napoléon", "Mariage", 1, {umusi},200000 )
            """)

con.commit()

con.close()
