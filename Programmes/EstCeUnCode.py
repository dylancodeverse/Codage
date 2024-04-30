def estCeUnCode (langageListe :list[str]) ->bool:
    listanaL = [langageListe]
    l1= eliminateEpsilon( residuel(langageListe,langageListe))
    if (len(l1)==0):
        return False
    listanaL.append(l1)
    while True :
        lnplusun = unionlangage(residuel(langageListe,listanaL[-1]), residuel(listanaL[-1],langageListe))
        if 'epsilon' in lnplusun:
            return False         
        for a in listanaL :
            if lnplusun == a :
                return True
        listanaL.append(lnplusun)            


# ok
def residuel (langageListe : list[str] , langageListe2 :list[str]):
    listResiduel = []
    for a in langageListe:
        for b in langageListe2 :
            if b.startswith(a):
                r= (b.removeprefix(a)) 
                if(r==''):
                    listResiduel.append('epsilon')      
                else :
                    listResiduel.append(r)    

    # if(len(listResiduel)==0):
    #     listResiduel.append('')
    return list(set(listResiduel))

def eliminateEpsilon(langageListe : list[str]):
    rep =[]
    for a in langageListe :
        if a !='epsilon':
            rep.append(a)
    return rep

def unionlangage(langageListe : list[str] , langageListe2 :list[str]):
    for a in langageListe2:
        if a not in langageListe :
            langageListe.append(a)
    return langageListe            


print( estCeUnCode(['1','00','01','10']))


print(estCeUnCode(['000', '010', '011', '01001'])) 