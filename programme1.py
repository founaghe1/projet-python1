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
country = input("Entrez votre pays: ")
if country == "France":
    print("Welcome to France!")
elif country == "USA":
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

    
    