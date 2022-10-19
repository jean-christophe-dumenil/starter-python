def nombre( *paramètre):
    maliste = []

    for param in paramètre :
        if isinstance(param,(int)):
            maliste.append(param)
    for element in maliste :
        if element %2 == 0 :
            print(element)
nombre(12, 69, 85, 42, 56, 89, 90)