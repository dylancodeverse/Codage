from itertools import combinations

class SardinasPaterson:

    @staticmethod
    
    def  estCeUnCode (langageListe :list[str]) ->bool:

        listanaL = [langageListe]
        l1= SardinasPaterson.eliminateEpsilon( SardinasPaterson.residuel(langageListe,langageListe))
        if (len(l1)==0):
            return True

        listanaL.append(l1)
        while True :
            lnplusun = SardinasPaterson.unionlangage(SardinasPaterson.residuel(langageListe,listanaL[-1]), SardinasPaterson.residuel(listanaL[-1],langageListe))
            if 'epsilon' in lnplusun:
                return False         
            for a in listanaL :
                if lnplusun == a :
                    return True
            listanaL.append(lnplusun)            


    # ok
    @staticmethod            
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

    @staticmethod
    def eliminateEpsilon(langageListe : list[str]):
        rep =[]
        for a in langageListe :
            if a !='epsilon':
                rep.append(a)
        return rep
    @staticmethod
    def unionlangage(langageListe : list[str] , langageListe2 :list[str]):
        for a in langageListe2:
            if a not in langageListe :
                langageListe.append(a)
        return langageListe            


# print(SardinasPaterson.estCeUnCode(['1', '00110', '01', '11', '0', '10', '010', '0001011', '01011']))
# print(SardinasPaterson.estCeUnCode(['0', '0110', '001', '10100', '101011']))

# print( estCeUnCode(['1','00','01','10']))


# print(estCeUnCode(['000', '010', '011', '01001'])) 

# print(estCeUnCode(['0','01','101','110','11']))
print(SardinasPaterson.estCeUnCode(['0']))
# listTo = ['0','01','101','110']

def generateListToSuppr(nToSuppr,myList):
    listFinal =[]
    if nToSuppr == 1:
        return myList
    else :
        newList = (list(combinations(myList,nToSuppr)))
        for a in newList:        
            listFinal.append(list(a))
    return listFinal            

def suppr(myList , toSp):
    for x in toSp :
        for y in x:
            if x in myList:
                myList.remove(x)
    return myList

def getMinToSuppr(myList) :
    nToSuppr = 0
    while True :
        nToSuppr+=1
        listOfList= generateListToSuppr(nToSuppr,myList)
        for xx in listOfList:
            if SardinasPaterson.estCeUnCode(suppr(myList,xx)):

                print(xx)
                print('nanala:')
                print(nToSuppr)
                return


    
# (getMinToSuppr(['0','01','100','010']))    





