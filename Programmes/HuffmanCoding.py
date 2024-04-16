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

    print ("proba ="+ str(sorted_counts))
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

def encodeWithFileAndWrite (pathInput:str, pathOutput:str, pathDictionnaire:str):
    with open(pathInput,'r') as file:
        message = file.read()
        dictionnaire = coding(message)
        newMessage =translateText(message , dictionnaire)
        # 
        while len(newMessage) %8 == 0:
            newMessage+='0'
        bytesList = [int(newMessage[i:i+8],2) for i in range (0, len(newMessage),8)]
        
        bytearray = bytearray(bytesList)

        with open(pathInput ,'wb') as fileFinal:
            fileFinal.write(bytearray)
        # eto mbola tokony manoratra anaty dictionnaire


# print(coding('BCCDACCBDABCCDEAAEDA')) 

