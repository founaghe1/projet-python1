#les listes

ma_liste = [1, 2, 3, 4, 5]
print("ma liste es => ", ma_liste)

# Ajouter et supprimer des elements dans une liste

# append() pour ajouter une valeur
ma_liste.append(6)
print("ma liste avec append(6) est => ", ma_liste)
#extend() pour ajouter plusieurs valeurs
ma_liste.extend([7,8])
print("ma liste avec extend([7,8]) est => ", ma_liste)

#La methode remove() pour supprimer
ma_liste.remove(1)
print("ma liste avec remove(1) est => ", ma_liste)

print()
#Recuperer un element de la liste avec les indices (index)

ma_liste_1 = ["Python", "JavaScript", "PHP"]
print("ma liste 1 => ", ma_liste_1)
print(ma_liste_1[1])

print()
#Modifier un element de la liste
ma_liste_2 = ["Volvo", "BMW", "Ford"]
print("la voiture de Ford est => ", ma_liste_2[2])
ma_liste_2[2] = "Audi"
print("la voiture de Ford a ete remplacée par => ", ma_liste_2)
# La methode sort()
ma_liste_2.sort()
print("Ordre aphabetique de liste 2 : ", ma_liste_2)

print()
# Les slices "recuperer certains elements de la liste"
user_list = ["user_01", "user_02", "user_03", "user_04", "user_05", "user_06"]

print("Mes users: \n", user_list[0:-1])

# la methode pop() "enlever un element de la liste parrapport à son index (position)"
user_list.pop(2)
print("\nMes user apres pop() => ", user_list)
#reccuperer l'element supprimer
supprime = user_list.pop(1)
print("\nsupprimer => ", supprime)

#La methode join() pour joinder les elements d'une liste

list_phrase = ["Python", "est", "un", "langage", "de", "programmation"]
joindre = "_".join(list_phrase)
print("\nMa liste joint : ", joindre)

#Creer une liste a aprtire d'une chaine de caractere
chaine_carac = "Ceci est une chaine de caractere"
liste_chaine = chaine_carac.split()
print("\nliste des charachteres => ", liste_chaine)

# Les operateurs d'apprtenance ( in, not in )
users_liste = ["mohamed", "sarifou", "diallo"]

user_name = input("\nEntrez votre nom : ").lower()

if user_name in users_liste:
    print("Vous êtes connecté en tant que ", user_name)
else:
    print("Vous n'etes pas dans la liste des utilisateurs. Merci de vous inscrire")

print()

# 5h00mn