import numbers


nombre = int(input("veuillez saisir un nombre entier"))
with open("data.txt, "r"") as fichier : 
    line = fichier.read()

listing = line.split()

nb_mots = 0

for element in listing :
    if len(element) == nombre :
        nb_mots == nb_mots+1
print(nb_mots)