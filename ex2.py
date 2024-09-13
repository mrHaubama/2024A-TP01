# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.


water_quantity = float(input("Quelle quantité d'eau faut-il assainir ? "))

def ressource_nécessaire(qt_eau):
    multi= qt_eau/5
    
    nb_filtre= 1*multi
    
    if nb_filtre%1 > 0:
        nb_filtre = int(nb_filtre+1)

    else:
        nb_filtre =int(nb_filtre)

    nb_lampsUV = 3*multi
    
    if nb_lampsUV %1 > 0:
        nb_lampsUV = int(nb_lampsUV+1)
    
    else:
        nb_lampsUV =int(nb_lampsUV)
    
    nb_kgChlore = 0.5*multi
    
    return nb_filtre, nb_lampsUV, nb_kgChlore

def retour_message(x,y,z):
    print("Voici les éléments requis pour assainir ", water_quantity,"L d'eau:\n\t- Filtre(s) : "+str(x)+"\n\t- Lampe(s) UV : "+str(y)+"\n\t- Chlore : "+str(z)+"kg\n") 

filtre, lamp, chlore = ressource_nécessaire(water_quantity)
retour_message(filtre, lamp, chlore)
