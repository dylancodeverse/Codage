def base10EnAutreBase (basecible:int , nombre:int):
    # division successive
    reste = []
    nombre= int(nombre / basecible)
    while nombre >= basecible :
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

print(enBase10('AB',16, {'A':10, 'B':11, 'C':12 ,'D':13, 'E':14, 'F':15 } )) 



def binaireEnHexadecimalMethodeBloc ():