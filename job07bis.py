for i in range (1, 100 ):
    message = ""; #Message à afficher, initialement vide
if  % 3 == 0 :
    #Nombre divisible par 3 : on ajoute "Fizz" au message
    ptint ("Fizz")
if nombre % 5 == 0 :
    #Nombre divisible par 5 : on ajoute "Buzz" au message
    message += 'Buzz'
if message == "" :
    #Si message est vide, le nombre n'est divisible ni par 3, ni par 5 :
    #le message affiché sera le nombre
    message = nombre
    console.log(message)