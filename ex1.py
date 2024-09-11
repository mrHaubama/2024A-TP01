# TODO: Créer un script permettant le formattage du livre des records des JO.
#Demander la nationalité de l'athlète
#Demander le nom de l'athlète
#Demander la date du record, la discipline, la catégorie, qui peut être nulle, le record

 

athlete = input("Quel est le nom de l'athlete ?")
country = input("De quelle nationalité est l'athlète ? ")
date = input("Quelle est la date du record ?") 
discipline= input ("Dans quelle discipline ?")
categorie= input("Quelconque categorie ?")
record = input ("quel est le record ?")
nouveau_record= print ("le nouveau record: \n ----------------- \n ", date, "\n", discipline, "-", categorie, "\n", athlete, country, "-", record)
