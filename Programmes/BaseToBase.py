def base10EnAutreBase (basecible:int , nombre:int , dictionnaire :dict):
    # division successive
    reste = []
    nombre= int(nombre / basecible)
    while nombre >= basecible :
        if dictionnaire.get(str (nombre%basecible)) != None :
            reste.insert(0,dictionnaire.get(str(nombre%basecible)))
        else:    
            reste.insert(0,str(nombre%basecible))
        nombre= int (nombre /basecible)

    reste.insert(0,str (nombre))
    return ''.join(reste)

# print(base10EnAutreBase(2,35)) 


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

# print(enBase10('AB',16, {'A':10, 'B':11, 'C':12 ,'D':13, 'E':14, 'F':15 } )) 


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

print(binaireEnOctalMethodeBloc('1010001'))


