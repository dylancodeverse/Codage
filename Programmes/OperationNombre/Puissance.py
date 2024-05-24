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

# print(evaluationEnBaseDecimaleRuffiniHorner('1',2)) 


depart = 0
div =[2,2,2,4,4,4,8,8,8,8,8]
a=0
for i in range (3,11):
    depart +=  puissanceIterative(2,i)/div[a]
    a+=1
    print(str(puissanceIterative(2,i))+"de lasa"+str(puissanceIterative(2,i)/div[a])+"ka manome"+str(depart))

# print(254*sum([1,2,3,4,5,6,7,8,9,10]))    

# print(puissanceRecursive(2 ,6) )    