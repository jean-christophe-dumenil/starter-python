def nombre( *paramètre):
    maliste = []

    for param in paramètre :
        if isinstance(param,(int)):
            maliste.append(param)
            maliste.sort()
    print(maliste)
nombre(102, 54, 0, 2, 98, 4125)