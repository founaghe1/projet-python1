password = input("Entrez un mot de passe : ")

if len(password) >= 8 and not password.isdigit():
    print("Mot de passe valide !")
elif password.isdigit():
    print("Le mot de passe ne contient que des entiers.")
elif password == "":
    print("Le mot de passe ne peut pas être vide.")
else:
    print("Le mot de passe doit contenir au moins 8 caracteres.")