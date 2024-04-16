from collections import deque

class BinaryTree:
    def __init__(self,value,freq,leftChild=None, rightChild=None, parent=None,arete=None ) ->  None:
        self.value = value
        self.freq = freq
        self.leftChild = leftChild
        self.rightChild =rightChild
        self.parent = parent
        self.arete = arete


def coding(message :str):
    # nodes ana prob miaraka amle caractere tries desc
    NodeDeProb = charcountDESC(message)
    leafMarked = []
    while len(NodeDeProb) != 1:
        # jerena ny min anakiroa anle nodeDeProb
        min0 ,min1 = NodeDeProb[len(NodeDeProb)-2], NodeDeProb[len(NodeDeProb)-1]
        # mi former node vaovao as newNode
        newNode = BinaryTree(min0.value+min1.value,min0.freq+min1.freq,min1,min0)
        # ovaina ny parent anle min anakiroa
        min0.parent = newNode
        min1.parent = newNode
        # petahana lay valeur anle arete
        min0.arete = 1
        min1.arete=0
        # fafana tao anaty nodedeprob ilay min anakiroa
        NodeDeProb= NodeDeProb[:-2]
        # ezahina atsofoka ao anaty ilay list nodeDeProb ilay node vaovao
        NodeDeProb=insert_sorted(NodeDeProb,newNode)
        if min0.leftChild is None :
            leafMarked.append(min0)
        if min1.leftChild is None:
            leafMarked.append(min1)
    # creer le dictionnaire des encodages
    dictionnaireDesEncodages = {}
    for xx in leafMarked :
        code = str(xx.arete)
        parent = xx.parent
        while parent.arete is not None :
            code =  str(parent.arete) + code 
            parent = parent.parent
        dictionnaireDesEncodages[xx.value]=code

    return dictionnaireDesEncodages
            


def charcountDESC(message:str)->list[BinaryTree]:
    counts = {}
    for char in message:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
     # trier le dictionnaire par ordre desc des valeurs
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    # Creer une liste de BinaryTree 
    binary_trees = []
    for char, freq in sorted_counts.items():
        binary_tree = BinaryTree(char, freq)
        binary_trees.append(binary_tree)

    return binary_trees



def insert_sorted(lst:list[BinaryTree], val:BinaryTree):
    index = 0
    while index < len(lst) and lst[index].freq >= val.freq: 
        index += 1
    lst.insert(index, val)
    return lst

def translateText(message :str , dictionnaire :dict) :
    resp = ''
    for a in message :
        resp += dictionnaire[a]
    return resp        


def formatDict(dictionnaire :dict):
    rep =''
    for key in dictionnaire.keys():
        rep+= key+ dictionnaire[key] +' '       
    return rep[:-1]


def encodeWithFileAndWrite (pathInput:str, pathOutput:str, pathDictionnaire:str):
    with open(pathInput,'r') as file:
        message = file.read()
        dictionnaire = coding(message)
        newMessage =translateText(message , dictionnaire)
        # fill par 0 mba ho feno araka ilay mandeha par 8 bits
        debordementcount = 0
        while len(newMessage) %8 != 0:
            newMessage+='0'
            debordementcount+=1
        bytesList = [int(newMessage[i:i+8],2) for i in range (0, len(newMessage),8)]
        byteArray = bytearray(bytesList)
        # stocker-na ilay izy compressed 
        with open(pathOutput ,'wb') as fileFinal:
            fileFinal.write(byteArray)
        # formater le dictionnaire
        newDictionnaireFormat =formatDict(dictionnaire)
        # stockage du dictionnaire et le debordement a la fin
        with open(pathDictionnaire,'w')  as dictFile :
            dictFile.write(newDictionnaireFormat+' '+str(debordementcount))           


def dicoParse(dico :str):
    # efa tsisy anle debordement intsony
    response = {}
    i=0
    while i < len(dico) :
        # alaina ny caractere voalohany
        key= dico[i]
        i+=1
        # alaina ny manaraka rehetra jusqu'a espace voalohany
        code =''
        while i!=len(dico) and dico[i]!= ' ':
            code+=dico[i]
            i+=1
        response[code]=key
        i+=1
    return response

def decodeFromDictionaryAndCompressedFile (compressedFilePath :str, dicoPath: str):
    with open (dicoPath,'r') as dicoFile:
        dicoCode = dicoFile.read()
        # alaina lay partie mi deborde
        debordementCount = int(dicoCode[len(dicoCode)-1])
        # reformat dicoCode sans debordement
        dicoCode = dicoCode[:-2]
        # le transformer en dico
        dictionnaire = dicoParse(dicoCode)

    with open(compressedFilePath,'rb') as cpFile:
        contenu = cpFile.read()
        # avadika en liste ana entier lay octets:
        bytesList = list(contenu)
        binaryString = ''.join(format(byte, '08b') for byte in bytesList)
        # tsy alaina izany ny partie debordee amle binaryString
        binaryString = binaryString[:-1*debordementCount]

    # tetezina amzay ilay binaryString de sady mijery anle dictionnaire eo ampi decode azy
    key =''        
    decodedMessage = ''
    for caract in binaryString:
        key+=caract
        # print(dictionnaire)
        try:
            decodedMessage+=dictionnaire[key]
            key =''
        except: pass            
    return decodedMessage        


# print(coding('BCCDACCBDABCCDEAAEDA')) 
                

# encodeWithFileAndWrite('C:/Users/MISA/Desktop/Workspace/S6/Codage/Programmes/input.txt','C:/Users/MISA/Desktop/Workspace/S6/Codage/Programmes/output.txt', 'C:/Users/MISA/Desktop/Workspace/S6/Codage/Programmes/dict.txt')

print( decodeFromDictionaryAndCompressedFile('C:/Users/MISA/Desktop/Workspace/S6/Codage/Programmes/output.txt', 'C:/Users/MISA/Desktop/Workspace/S6/Codage/Programmes/dict.txt'))