def base10EnAutreBase (basecible:int , nombre:int , dictionnaire :dict):
    # division successive
    reste = []
    while nombre !=0 :
        if dictionnaire !=None and dictionnaire.get(str (nombre%basecible)) != None :
            reste.insert(0,dictionnaire.get(str(nombre%basecible)))
        else:    
            reste.insert(0,str(nombre%basecible))
        nombre= int (nombre /basecible)

    return ''.join(reste)

# print(base10EnAutreBase(8,81,None)) 


# mbola tsy mazaka anle misy lettre
def enBase10(nombre:str, baseDOrigine:int , dictionnaire :dict ):
    resultat = 0
    i=0
    nombre= nombre[::-1]
    for x in nombre:
        try:
            resultat += int(x) * (baseDOrigine **i)
        except ValueError:
            resultat+= dictionnaire.get(x) * (baseDOrigine **i)
        i+=1
    return resultat

# print(enBase10('1010001',2, {'A':10, 'B':11, 'C':12 ,'D':13, 'E':14, 'F':15 } )) 


def binaireEnHexadecimalMethodeBloc (nombre:str, dictionnaire = {'A':10, 'B':11, 'C':12 ,'D':13, 'E':14, 'F':15 } ):    
    # diviser nombre en bloc de quatres
    blocs_inverses = [nombre[::-1][i:i+4] for i in range(0, len(nombre), 4)]
    blocs_originaux = [bloc[::-1].zfill(4) for bloc in blocs_inverses]
    blocs_originaux = blocs_originaux[::-1]
    # 
    resultat= []
    for bloc in blocs_originaux :
        resultat.append(str( enBase10(bloc ,2,None)))

    return ''.join(resultat)        

# print(binaireEnHexadecimalMethodeBloc('1010001'))

def binaireEnOctalMethodeBloc (nombre:str):    
    # 8 etant 2**3
    blocs_inverses = [nombre[::-1][i:i+3] for i in range(0, len(nombre), 3)]
    blocs_originaux = [bloc[::-1].zfill(3) for bloc in blocs_inverses]
    blocs_originaux = blocs_originaux[::-1]
    resultat= []
    for bloc in blocs_originaux :
        resultat.append(str( enBase10(bloc ,2,None)))

    return ''.join(resultat)        

# print(binaireEnOctalMethodeBloc('1010001'))

# ------------------------
def est_puissance(B, A):
    # Vérifier si A est égal à 1, car B^0 = 1 pour tout B différent de 0
    if A == 1:
        return True, 0

    # Initialiser x à 1
    x = 1
    # Initialiser la valeur de B^x
    puissance = B

    # Tant que la puissance est inférieure à A
    while puissance < A:
        # Incrémenter x
        x += 1
        # Calculer la nouvelle puissance de B
        puissance *= B

    # Si la puissance est égale à A, alors A est une puissance de B
    if puissance == A:
        return True, x
    else:
        return False, None
# ------------------------

def baseToBaseMethodBloc (nombre :str , baseDorigine:int, dictionnaireBaseDorigine :dict , baseCible:int, dictionnaireBaseCible:dict):
    # verifier si on peut utiliser la methode en bloc
    prediction , p = est_puissance(baseDorigine ,baseCible)
    if prediction:
        blocs_inverses = [nombre[::-1][i:i+p] for i in range(0, len(nombre), p)]
        blocs_originaux = [bloc[::-1].zfill(p) for bloc in blocs_inverses]
        blocs_originaux = blocs_originaux[::-1]
        resultat= []
        for bloc in blocs_originaux :
            b10 = str(enBase10(bloc ,baseDorigine,dictionnaireBaseDorigine))
            if dictionnaireBaseCible != None and  dictionnaireBaseCible.get(b10):
                resultat.append( dictionnaireBaseCible.get(b10))
            else:
                resultat.append(b10)
        return ''.join(resultat)        
    else :
        raise ValueError('methode bloc impossible')

# print(baseToBaseMethodBloc('1010001',2,None ,8,None))

def baseToBasePassantParLaBase10 (nombre :str , baseDorigine:int, dictionnaireBaseDorigine :dict , baseCible:int, dictionnaireBaseCible:dict):
    try:
        return baseToBaseMethodBloc(nombre , baseDorigine , dictionnaireBaseDorigine,baseCible ,dictionnaireBaseCible)
    except ValueError:
        nombreEnBase10 = enBase10(nombre,baseDorigine,dictionnaireBaseDorigine)
        return base10EnAutreBase(baseCible,nombreEnBase10, dictionnaireBaseCible)

print(baseToBasePassantParLaBase10('1010001' , 2 ,None , 8 ,None))

