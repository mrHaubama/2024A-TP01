# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level =float(input("Pourcentage de batterie ? "))

def distance_restant(entre):
    distance = 0
    bat= entre
    while bat != 0:
        if bat > 50:
            reste= bat-50
            bat = 50
            distance += (2*reste)
        elif 50>= bat > 25:
            reste= bat-25
            bat = 25
            distance += (0.5*reste)
        elif 25 >= bat >10:
            reste= bat-10
            bat =10
            distance += 1*reste
        elif 10 >= bat > 5:
            reste= bat-5
            bat = 5
            distance += (2.5*reste)
        elif 5 >= bat > 0:
            distance += (6*bat)
            bat =0
    return distance 

if battery_level != 0:

    print(distance_restant(battery_level), "km")
else :
    print("La batterie est vide")