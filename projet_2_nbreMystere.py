#Le nombre mystrere
import random

def jeu_nombre_mystere():
    nombre_mystere = random.randint(0, 100)
    essais_restants = 5

    print("Bienvenue dans le jeu du nombre mystère !")
    print("Devinez le nombre mystère entre 0 et 100.")

    while essais_restants > 0:
        try:
            guess = int(input("Entrez votre guess : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if guess == nombre_mystere:
            print(f"Félicitations ! Vous avez trouvé le nombre mystère {nombre_mystere} en {5 - essais_restants + 1} essais.")
            break
        elif guess < nombre_mystere:
            print("Le nombre mystère est plus grand.")
        else:
            print("Le nombre mystère est plus petit.")

        essais_restants -= 1
        print(f"Il vous reste {essais_restants} essai{'s' if essais_restants > 1 else ''}.")

    if essais_restants == 0:
        print(f"Désolé, vous n'avez pas trouvé le nombre mystère. La réponse était {nombre_mystere}.")

# Appeler la fonction pour démarrer le jeu
jeu_nombre_mystere()

