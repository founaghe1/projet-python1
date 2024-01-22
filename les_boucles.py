# La boucle for
print("La boucle for")

for i in range(3):
    print("La boucle for de : ", i)
    i += 1

print()

liste = [4, 7, 6, 25, 17, 5, 10]
liste.sort()
print("La liste triée est :", liste)
for i in liste:
    print("Ma valeur a l'index :", liste.index(i), "est", i)
    
    
# La boucle while
print("\nLa boucle while")

i = 0
while i < len(liste):
    print("La boucle while de :", i, "valeur :", liste[i])
    i += 1
    
print()

continuer = "o"
continuer = input("Voulez-vous continuer ? o/n : ")
while continuer == "o":
    print('Okay, nous continuons....')
    continuer = input("Voulez-vous continuer ? o/n : ")
    
# l'instruction continue
print("\nL'instruction continue")
liste_1 = ["1", "5", "2", "Diallo", "8", "1Moha", "0",]

for i in liste_1:
    if i.isdigit():
        continue
    print("Ceci n'est pas un nombre :", i)
    
    
#Comprehension des listes
print("\nComprehension des listes")

liste_2 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print("Liste entiere :", liste_2)
nombres_positifs = [i for i in liste_2 if i > 0]
print("Nombres positifs :", nombres_positifs)