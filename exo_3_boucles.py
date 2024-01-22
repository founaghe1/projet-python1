for i in range(10):
    print(f"Utilisateur {i+1}")
    
    
#reverse
print('\nMot inverser avec la methode reversed()')

mot = "python"
#reversed(mot)
for i in reversed(mot):
    print(i)
    

#Calculatrice
print("\nCalculatrice")

a = b = ""
while not (a.isdigit() and b.isdigit()):
    a = input("\nEntrez une premiere valeur : ")
    b = input("Entrez une deuxieme valeur : ")
    if not (a.isdigit() and b.isdigit()):
        print("Ces valeurs ne sont pas numeriques.")
        
print(f"La somme de {a} et {b} est egale à : { int(a) + int(b)}")

