# TODO: Créer un script permettant le formattage du livre des records des JO.
#Demander la nationalité de l'athlète
#Demander le nom de l'athlète
#Demander la date du record, la discipline, la catégorie, qui peut être nulle, le record

 

country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est son nom ? ")
date = input("Date du record ? ") 
discipline= input ("Dans quelle discipline ? ")
categorie= input("Dans une catégorie spécifique ? ")
record = input ("Quel est le record ? ")
nouveau_record= print ("\nNouveau Record:\n--------------------\n"+date,"-",discipline,"-",categorie+":\n\t"+athlete,"("+country+")","-", record)
