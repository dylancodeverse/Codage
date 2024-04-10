def puissanceIterative(nombre, puissance):
    resultat =1 
    for i in range (0,puissance):
        resultat= resultat*nombre
    return resultat

# print(puissanceIterative(4,0))    

def puissanceRecursive(nombre ,puissance):
    resultat=1
    if puissance!=0:
        resultat= nombre * puissanceRecursive(nombre , puissance-1)
    return resultat

