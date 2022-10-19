Fichier = open("output.txt", "w+")

Fichier.write("Salut tout le monde")

Fichier.close()

with open("output.txt", "r") as fichier:
	print (fichier.read())