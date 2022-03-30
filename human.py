#générateur d'enfant ;)

from random import choice, randint
import sqlite3


#  db = sqlite3.connect("humans.db")
# cur = db.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS humans(gender TEXT, hairs TEXT, name TEXT)")

class Human():
    def __init__(self):
        self.gender = ["masculin", "feminin", "mutant"]
        self.hair_color = ["brun", "noir", "blond", "chatain", "roux"]

        self.choiced_gender = choice(self.gender)
        self.choiced_hair_color = choice(self.hair_color)


    if self.choiced_gender == "masculin":
        print("C'EST UN GARCON !!!")
        name = input("comment voulez vous appelez votre unique enfant \n")
        print(f"votre enfant {name} est de sexe {self.choiced_gender} et a les cheveux {self.choiced_hair_color} !")
        db = sqlite3.connect("humans.db")
        cur = db.cursor()
        cur.execute(f"INSERT INTO humans VALUES (masculin, {self.choiced_hair_color},  {name})")

    elif sexe == "feminin":
        print("C'EST UNE FILLE !!!")
        name = input("comment voulez vous appelez votre unique enfant \n")
        print(f"votre enfant {name} est de sexe {self.choiced_gender} et a les cheveux {self.choiced_hair_color} !")
        db = sqlite3.connect("humans.db")
        cur = db.cursor()
        cur.execute(f"INSERT INTO humans VALUES (feminin, {self.choiced_hair_color},  {name})")

    else:
        rep = input("Votre enfant est un mutant mais vous voulez quand même lui donner un nom ? (oui/non)\n")

        if rep == "oui":
            name2 = input("comment s'appelle t-il ?\n")
            print(f"daccord votre enfant mutant s'appelera {name2}")
            db = sqlite3.connect("humans.db")
            cur = db.cursor()
            cur.execute(f"INSERT INTO humans VALUES (mutant, {self.choiced_hair_color},  {name})")
        
        else:
            db = sqlite3.connect("humans.db")
            cur = db.cursor()
            cur.execute(f"INSERT INTO humans VALUES (mutant, {self.choiced_hair_color},  nul)")
            print("Je pense que c'est mieux comme sa aussi :)")


def show_all_kids():
        db = sqlite3.connect("humans.db")
        cur = db.cursor()
        cur.execute(f"SELECT * FROM humans")
        res = cur.fetchall()
        for res in res:
            print(res)

show_kids = input("Veux-tu afficher tes enfants ? (oui/non)")
if show_kids == "oui":
    show_all_kids()
else:
    Human()
