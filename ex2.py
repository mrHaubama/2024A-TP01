# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = float(input("Quelle quantité d'eau faut-il assainir ? "))


multi= water_quantity/5

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




reponse = f"""Voici les éléments requis pour assainir {water_quantity}L d'eau:
\t- Filtre(s) : {nb_filtre}
\t- Lampe(s) UV : {nb_lampsUV}
\t- Chlore : {nb_kgChlore}kg"""

print(reponse)
