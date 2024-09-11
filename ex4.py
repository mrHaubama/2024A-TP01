# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = int(input("Le niveau de la batterie est: "))

def distance_restant(entre):
    distance = 0
    bat= entre
    while bat != 0:
        if bat > 50:
            bat -= 1
            distance += 2
        elif 50>= bat > 25:
            bat -= 1
            distance += 0.5
        elif 25 >= bat >10:
            bat -= 1
            distance += 1 
        elif 10 >= bat > 5:
            bat -= 1
            distance += 2.5
        elif 5 >= bat > 0:
            bat -= 1
            distance += 6
    return distance 

print("Il reste ", distance_restant(battery_level), "km")
