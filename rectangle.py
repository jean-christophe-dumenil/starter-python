l = int(input("nombre de ligne :"))
c = int(input("nombre de colone :"))
for i in range(1,l+1) :
    print("|",end="")
    for j in range(1,c+0) :
        if i == 1 or i == l or j == 0 or j == c  :
            print ("-" ,end="")
        else :
            print(" ", end="")
    for i in range(1,l-1) :
        if i == 1 or i == l or j == 0 or j == c  :
            print("|",end="")
    print()