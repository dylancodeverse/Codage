# question 1 : programme permettant d’avoir les
# codes de chaque si de S selon le codage de Huffman

class BinaryTree:
    def __init__(self,value,freq,leftChild=None, rightChild=None, parent=None,arete=None ) ->  None:
        self.value = value
        self.freq = freq
        self.leftChild = leftChild
        self.rightChild =rightChild
        self.parent = parent
        self.arete = arete


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

# programme qui prend en paramètre un mot/texte de S et renvoie le mot/texte codé par le codage de Huffman précédent

def translateText(message :str , dictionnaire :dict) :
    resp = ''
    for a in message :
        resp += dictionnaire[a]
    return resp        

def messageToCodedMessage (message :str ):
    dictionnaire = coding(message)
    newMessage =translateText(message , dictionnaire)
    return newMessage 

# un programme qui prend en paramètre un mot/texte codé selon le codage de Huffman
# de la question 1:(a) et renvoie le mot/texte initial.
def decodeMessage(encodedMessage: str , dictionnaire :dict):
    key =''        
    decodedMessage = ''
    for caract in encodedMessage:
        key+=caract
        # print(dictionnaire)
        try:
            decodedMessage+=dictionnaire[key]
            key =''
        except: pass
    return decodedMessage


# Soit t un texte en anglais dans un fichier texte.txt. Proposez une façon de compresser le
# texte en utilisant le codage de Huffman. Implanter votre proposition.


    