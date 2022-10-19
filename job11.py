fichier = open('domains.xml', 'r') 
lignes=fichier.readlines()
texte=''.join(lignes)
mots=texte.split()
repetitions=[]
for domain in mots:
    dedans=0
    for repet in repetitions: #on regarde si le mot est déjà dans la listes des mots répétés (repetion)...
        if repet[0]==domain: # ...si ce mot est déjà dans répétions, on augmente son nombre d’apparitions de 1
            repet[1]+=1
            dedans=1
            break
    if dedans==0: # ... et s'il n'est pas déjà dedans, on le rajoute et on règle son nombre d'apparitions à 1.
        repetitions.append([domain,1])
print(len(repetitions))
fichier.close()