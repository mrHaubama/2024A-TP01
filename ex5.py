#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#Attention si la chaîne est invalide, un message d'erreur est attendu.




country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")
code_medals = code_medals.lower()

def Table_medals(code_medals):
    if not all(char in "gbs" for char in code_medals):
        print("Ceci est une chaine invalide.")
        return
    if "g" in code_medals:
        count_g = code_medals.count("g")
        print(f"{country}:")
        print(f"- {count_g} Or")
    if "s" in code_medals:
        count_b = code_medals.count("s")
        print("-",count_b,"Argent")
    if "b" in code_medals:
        count_s = code_medals.count("b")
        print("-",count_s,"Bronze")


(Table_medals(code_medals))



