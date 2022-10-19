L = int(input("Veuillez saisir le nombre de lignes :"))
a = 0 
for j in range(L,1,-1):
    print(" " * j + "/" + " " * a * 2 + "\\")
    a += 1
print(" /" + "__" * (L - 1) + "\\")