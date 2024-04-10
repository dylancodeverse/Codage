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

def puissanceExponentiation(nombre, puissance):
    if puissance==0:
        return 1
    elif puissance==1:
        return nombre
    elif puissance%2==0:
        return puissanceExponentiation(nombre*nombre,puissance/2)
    else :
        return puissanceExponentiation(nombre*nombre ,(puissance-1)/2)

# print(puissanceExponentiation(4,2))    
def evaluationEnBaseDecimaleRuffiniHorner(nombre :str , baseDOrigine:int):
    if len(nombre)== 1:
        return int(nombre) 
    v0 = int(nombre[0])*baseDOrigine + int( nombre[1])
    for lettre in nombre[2::]:
        v0 = v0 *baseDOrigine + int( lettre)
    return v0                

print(evaluationEnBaseDecimaleRuffiniHorner('1',2)) 