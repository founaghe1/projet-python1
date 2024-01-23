# Liste des courses
import sys

liste = []

while True:
    print("\nChoisissez parmi les 5 options suivantes :")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément de la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        # Ajouter un élément à la liste
        element = input("Entrez l'élément à ajouter : ")
        liste.append(element)
        print(f"{element} a été ajouté à la liste.")

    elif choix == "2":
        # Retirer un élément de la liste
        if liste:
            print("Liste actuelle :", liste)
            element = input("Entrez l'élément à retirer : ")
            if element in liste:
                liste.remove(element)
                print(f"{element} a été retiré de la liste.")
            else:
                print(f"{element} n'est pas dans la liste.")
        else:
            print("La liste est vide.")

    elif choix == "3":
        # Afficher la liste
        if liste:
            print("Voici le contenu de la liste actuelle:")
            for i, element in enumerate(liste, 1):
                print(f"{i}. {element}")
        else:
            print("La liste est vide.")

    elif choix == "4":
        # Vider la liste
        if liste:
            liste.clear()
            print("La liste a été vidée.")
        else:
            print("La liste est déjà vide.")

    elif choix == "5":
        # Quitter
        print("Merci d'avoir utilisé la liste des courses. Au revoir!")
        sys.exit()

    else:
        print("Choix invalide. Veuillez entrer un nombre de 1 à 5.")
        
    print("_" * 50)
