''' 

#Les variables
salutation = "Bonjour, bienvenue sur mon site web"
print(salutation)
#On peut modifier la variable pour changer le texte affiché.
salutation = "Hello, welcome to my website."
print(salutation)


print()
#les integer
a = 10
b = 5
c = a + b
print("c => ", c)

d = a

# verifier l'emplacement d'un objet dans la memoire
id_variable_a = id(a)
id_variable_d = id(d)
id_variable_b = id(b)
print()
print("a => ", a)
print("d => ", d)
print()
print("place de a dans la memoire => ", id_variable_a)
print("place de d dans la memoire => ", id_variable_d)
print("place de b dans la memoire => ", id_variable_b)

# affectation d'un objet à un variable
# Simple
x = 4
y = 6

# Parallele
x, y = 4, 6

# Multiple
a = 5
b = 5
c = 5

a = b = c = 5 #Affectation multiple

print()

# Conversion des variables

a = "5"
print("a est un string: ", a)
# affiche le type de a
print("type de a :", type(a))

a = int(a)
print()

print("a est devenu int: ", a)
# affiche le type de a
print("type de a :", type(a))

print()
# Les inputs
print()
print("_____Les inputs_____")
#Afficher un message de bienvenue en fonction du pays d
country = input("Entrez votre pays: ").lower()
if country == "france":
    print("Welcome to France!")
elif country == "usa":
    print("Welcome to the USA!")
else:
    print("Bye")
print() 
#Demander à l'utilisateur son nom et afficher une phrase de bienvenue personnalisée.
name = input("Enter your name: ")
if len(name) > 0:
    print("Welcome", name + ", nice to meet you!")
else:
   print("Entrez un nom")
   


print()
# 2h 29 mn  
  
# Manupiler les chaines de caracteres
    # Changer la casse (A-a ou B-b)
print("Manupiler les chaines de caracteres")
print("Changer la casse (A-a ou B-b)") 
#upper()
Upper = input("Tappez un mot pour UPPER : ").upper()
print("Votre mot est en majuscule maintenant : ", Upper)

#lower()
Lower = input("Tappez un mot pour LOWER : ").lower()
print("Votre mot est en minuscule maintenant : ", Lower)
  
#capitalize()
Capitalize = input("Tappez un mot pour CAPITALIZE : ").capitalize()
print("Votre mot est en Capitalize maintenant : ", Capitalize)

#title()
Title = input("Tappez un texte pour TITLE : ").title()
print("Votre mot est en TITLE maintenant : ", Title)

print()
    # Remplacer ou modifier des elements
#replace()
print("Remplacer ou modifier des elements")
Replace = "Bonjour".replace("jour", "soir")
print("Avec REPLACE Bonjour devient => ", Replace)

ReplaceMultiple = "Bonjour Bonjour".replace(" ", "").replace("jour", "soir")
print("Avec REPLACE enlevons l'espace et remplaçons => ", ReplaceMultiple)

#strip()
Strip = " Salut ".strip() #enleve les espace
print("En utilisant STRIP sans specifier des caracteres, le résultat est : ", Strip)

Strip_2 = " Bonjour ".strip(" ujor") #enleve l'espace du debut et les caracteres
print("strip_2 enleve l'espace du debut et les caracteres :", Strip_2)

#rstrip()
Rstrip = " Bonjour ".rstrip(" ujor") #rstrip agit vers la droite
print("rstrip enleve l'espace et les caracteres vers la droite :", Rstrip)

#lstrip()
Lstrip = " Bonjour ".lstrip(" ujor") #lstrip agit vers la gauche
print("lstrip enleve l'espace et les caracteres vers la gauche :", Lstrip)

print()
    #Separer et joindre
print("Separer et joindre")
#split()
Split = "1, 2, 3, 4, 5".split(", ")
print("Split de 1, 2, 3, 4, 5 => ", Split)

#joindre()
Join = "-".join("1, 2, 3, 4, 5".split(", "))
print("Join de '-'.join('1, 2, 3, 4, 5'.split(", ")) => ", Join)

print()
    #Remplir de zéros
print("Zfill ou Remplir de zéros")

Zfill = "5".zfill(4)
print("zfill(4) de 5 => ", Zfill)
Zfill_2 = "5".zfill(3)
print("zfill(3) de 5 => ", Zfill_2)

for i in range(1, 1000+1):
    print(str(i).zfill(3))


print()
    # Les methodes " is "
print("Les methodes is")

#islower()
is_lower = "bonjour".islower()
print("islower de bonjour => ", is_lower)

#isupper()
is_upper = "BonjOuR".isupper()
print("isupper de BonjOuR => ", is_upper)
is_upper_1 = "BONJOUR".isupper()
print("isupper de BONJOUR => ", is_upper_1)

#isdigit()
is_digit = "50".isdigit()
print("isdigit de '50' =>", is_digit)
is_digit_1 = "20a".isdigit()
print("isdigit de '20a' => ", is_digit_1)

print()
    #Compter le nombre d'occurrences dans chaine de caracteres
#count()
print("Compter le nombre d'occurrences dans chaine de caracteres")
NbOccurence = "Bonjour Bonjour".count("Bonjour")
print("Le nombre d'occurence de BONJOUR dans NbOccurence est : ", NbOccurence)
NbOccurence_1 = "Bonjour jour".count(" jour")
print("Le nombre d'occurence de JOUR est : ", NbOccurence_1)

print()
    #Rechercher 'l'index' d'un mot ou une suite de caracteres
print("Rechercher 'l'index' d'un mot ou une suite de caracteres")
find = "Bonjour le jour".find("jour")
print("trouve jour => ", find)
index = "Bonjour le jour".index("le")
print("trouve le avec index => ", index)
    
    
    
Chaine = "Ceci est une petite phrase pour tester la recherche"
MotATrouver = "petite"
if MotATrouver.lower() in Chaine.lower():
    print("Le mot '%s' est present dans la chaine." % MotATrouver)
else:
    print("mot non trouer")
    

print()
#Trouver le debut ou la fin de chaine
fin = "image.png".endswith(".png")
print("le format de l'image est en PNG => ", fin)
start = "image.png".startswith("video")
print("la chaine 'image.png' commence par video =>", start)

print()
#Les oprateurs
print("Les operateurs")
    #Les operateurs mathematiques
print("Les operateurs mathematiques")
print("Affiche 5 + 2 =", 5 + 2)
print("Affiche 5 - 2 =", 5 - 2)
print("Affiche 5 * 2 =", 5 * 2)
print("Affiche 5 / 2 =", 5 / 2)

    #Sur une chaine de caractere
python = "Python"
print(f"Affiche le mot {python} 3 fois : ", python * 3)

#Le modulo %
rest = 7 % 4
print("La division de 7 par 4 donne un reste de : ", rest)
# le quotient //
quotient_1 = 10 / 3
print("le quotient de 10 et 3 est : ", quotient_1)
quotient = 10 // 3
print("le quotient de 10 et 3 est : ", quotient)
# la puissance **
puissance = 8**3
print("8 a la puissance de 3 est : ", puissance)

    #les operateurs d'assignation
    
x=5
print("Affiche la valeur assignée a x => ", x)
x += 1
print("Apres l'ajout de 1 a x on obtient : ", x)

    #les operateurs de comparaison
m = 12
n = 6
if m > n:
    print("m est superieur a n")
else:
    print("m est inferieur à n")
    
    
print()
#Le formatage des chaines de caracteres
print("Le formatage des chaines de caracteres")
    # La concatenation
print("Bonjour" + "tout" + "le monde")
    # les f-string
nom = "Gueye"
print(f"le nom {nom} ne figure pas dans notre base de donnée")
    # La methode format
mon_age = 25
phrase = "je suis agé de {age} ans".format(age=mon_age)
print(phrase)
phrase_2 = "je suis agé de {0} ans, {0} n'est pas trop vieu!".format(mon_age)
print(phrase_2)

name = "Mohamed"
age = 27
phrase_3 = "Mon nom est {0}, je suis agé de {1} ans.".format(name, age)
print(phrase_3)
'''
#3h 30mn
print()

#Les structures conditionnelles
print("LES STRUCTURES CONDITIONNELLES")
# Les if else
# cas1
print("CAS-1")
verifie_number = int(input("Entrez un entier : "))

if verifie_number > 18:
    print("L'entier entré est superieur à 18. \nMercii !!")
elif verifie_number == 18:
    print("L'entier entre est égal à 18.")
else:
    print("L'entier entré est inférieur à 18.")
    
# Cas 2
print("CAS-2")

users_liste = ["mohamed", "sarifou", "diallo"]

user_name = input("Entrez votre nom : ").lower()

if user_name in users_liste:
    print("Vous êtes connecté en tant que ", user_name)
else:
    print("Vous n'etes pas dans la liste des utilisateurs. Merci de vous inscrire")

# Cas 3
print("CAS-3")

password = input("Entrez un mot de passe : ")

if len(password) >= 8:
    print("Mot de passe valide !")
else:
    print("Le mot de passe doit contenir au moins 8 caracteres.")
    
# Les operateurs logiques (or; and et not)

if user_name in users_liste and len(password) > 8:
    print(f"Bonjour {user_name}, vous avez accés à notre site !")
else:
    print("Accès refusé, veuillez vérifier votre identité ou mot de passe")
    
        


print()
  