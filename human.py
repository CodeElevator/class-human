#générateur d'enfant ;)

from random import choice, randint

class human:
    sexe = ["masculin", "feminin", "mutant"]
    color = ["brun", "noir", "blond"]

    sexe = choice(sexe)
    color = choice(color)


    if sexe == "masculin":
        print("C'EST UN GARCON !!!")
        name = input("comment voulez vous appelez votre unique enfant \n")
        print(f"votre enfant {name} est de sexe {sexe} et a les cheveux {color} !")

    elif sexe == "feminin":
        print("C'EST UNE FILLE !!!")
        name = input("comment voulez vous appelez votre unique enfant \n")
        print(f"votre enfant {name} est de sexe {sexe} et a les cheveux {color} !")

    else:
        rep = input("Votre enfant est un mutant mais vous voulez quand même lui donner un nom ? (oui/non)\n")

        if rep == "oui":
            name2 = input("comment s'appelle t-il ?\n")
            print(f"daccord votre enfant mutant s'appelera {name2}")
        
        else:
            print("Je pense que c'est mieux comme sa aussi :)")


human()