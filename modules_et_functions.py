# Quelques modules et functions
import random  # Le module random
import os # le module os (pour supprimer ou creer des dossiers)
from pprint import pprint # affiche le resultat par ordre

# La fonction random.randint() qui renvoie un nombre aléatoire entier
print("La function randint()")
a = random.randint(0, 3)
print("la valeur est : ", a)

# La fonction random.randrange() qui renvoie un nombre aléatoire entier en interval
print("La function randrange()")
c = random.randrange(15)
print("La valeur est : ", c)
#randrang() avec step
d = random.randrange(0, 101, 5)
print("La valeur est 'avec step' :", d)

# La function uniform() qui renvoie un nombre aléatoire decimal 
print("La function uniform()")
b = random.uniform(0, 2)
print("la valeur est : ", b)

    # Le module os 
chemin = "Documents"

#joindre le notre dossier
mon_dossier = os.path.join(chemin, "mon-dossier", "test")
print("dossier créé : ", mon_dossier)

#creer le dossier makedirs()
if not os.path.exists(mon_dossier):
    os.makedirs(mon_dossier)
    
# OR
os.makedirs(mon_dossier, exist_ok=True)

#supprimer le dossier removedirs()
if os.path.exists(mon_dossier):
    os.removedirs(mon_dossier)

# Les functions dir et help

print("random : ", dir(random))
print()
#help(dir) 
#la function pprint()
print("Le module os : ")
pprint(dir(os))

print()
    # Les objets "callable"
    
print(callable(pprint))
print(callable(random))

    