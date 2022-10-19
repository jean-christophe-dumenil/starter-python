import re

fichier = open("data.txt","r")
texte = fichier.read()
pattern = '[a-zA-Z]+'
match = re.findall(pattern, texte)

print(len(match))