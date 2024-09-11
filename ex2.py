# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.


water_quantity = int(input("Quelle quantité d'eau doit être assainit?"))

def ressource_nécessaire(qt_eau):
    multi= qt_eau/5
    
    nb_filtre= 1*multi
    nb_lampsUV = 3*multi
    nb_kgChlore = 0.5*multi
    return nb_filtre, nb_lampsUV, nb_kgChlore

def retour_message(x,y,z):
    print("Voici les matériaux requis pour l'assainissement de 10L d'eau: \n\t - filtre: "+str(x)+"\n\t - lamp UV: "+str(y)+"\n\t - Chlore: "+str(z)+"kg") 

filtre, lamp, chlore = ressource_nécessaire(water_quantity)
retour_message(filtre, lamp, chlore)
