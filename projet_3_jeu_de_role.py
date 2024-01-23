import random

ENEMY_HEALTH = 50
PLAYER_HEALTH = 50
NUMBER_OF_POTIONS = 3
SKIP_TURN = False

while True:
    #jeu du joueur
    if SKIP_TURN:
        print("Vous passez votre tour...")
        SKIP_TURN = False
    else:
        user_choice = ""
        while user_choice not in ["1", "2"]:
            user_choice = input("Attaquer en cliquant (1) ⚔ ou \nUtiliser une potion en cliquant (2) 💕 : ")
            
        if user_choice == "1":
            damage = random.randint(5, 10)
            ENEMY_HEALTH -= damage
            print(f"Vous avez attaqué et infligé {damage} dégâts à l'ennemi ⚔")
        elif user_choice == "2":
            if NUMBER_OF_POTIONS > 0:
                health_potion = random.randint(15, 50)
                PLAYER_HEALTH += health_potion
                NUMBER_OF_POTIONS -= 1
                SKIP_TURN = True
                print(f"Vous recuperez {health_potion} points de vie ❤ ({NUMBER_OF_POTIONS} 🧪⚗ restantes)")
            else:
                print("Vous n'avez plus de potions 🧪!")
                continue
            
    if ENEMY_HEALTH <= 0:
        print("\nFélicitations 🎉 ! Vous avez vaincu l'ennemi 🦾💪")
        break
        
    #attaque de l'ennemi
    enemy_attack = random.randint(5, 15)
    PLAYER_HEALTH -= enemy_attack
    print(f"\nL'ennemi vous attaque avec {enemy_attack} points de degat ⚔ ")
        
    if PLAYER_HEALTH <= 0:
        print(f"\n Vous avez été tués 😰 !")
        break
        
    #stats
    print(f"\nVotre santé : {PLAYER_HEALTH} points de vie")
    print(f"Ennemi : {ENEMY_HEALTH} points de vie")
    print('-*-' * 15)
        
print("FIN DE LA PARTIE")