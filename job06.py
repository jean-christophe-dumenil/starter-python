from re import I


a=str(input(">"))
while a != "Au revoir" :
    if a == "Bonjour":
        print("Bonjour a toi")
    else:
        print(a)
       
    a = str(input(">"))