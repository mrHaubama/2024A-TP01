# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math

speed = float(input("Vitesse initiale (en ms/s): "))
angle = float(input("Angle de lancement (en degres): "))
distance =  (speed**2)*(math.sin(math.radians(2*angle))) / 9.8
rounded_distance_max = round(distance, 2)
print("la distance maximal en x est de",rounded_distance_max,"m")
