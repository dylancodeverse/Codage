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
    while NodeDeProb.count != 1:
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
    # manomboka eto amzay anh ,manao parcours anle graphe en profondeur de mi stocker anle etiquette
    pile =  deque()
    pile.append(NodeDeProb[0])
    lstArete = []
    marked = []
    dictionnaireDesEncodages = {}
    while(len(pile)!=0):
        lastIn = pile.pop()
        if lastIn not in marked :
            marked.append(lastIn)
            if lastIn.arete!=None:
                lstArete.append(lastIn.arete)
                # les voisiins du node
                if lastIn.lefChild is not None : # raha tsy leaf 
                    pile.append(lastIn.leftChild)
                    pile.append(lastIn.rightChild)
                else : # raha efa feuille
                    dictionnaireDesEncodages[lastIn.value]= "".join(str(x) for x in lstArete)

    return dictionnaireDesEncodages
            



# parcoursProfondeurIter(graphe G, sommet s)
#       p=creer_pile()
#       p.empiler(s)
#       tant que p est non vide
#          s=p.depiler()
#          si s n'est pas marqué
#             marquer le sommet s
#             afficher le sommet s
#             pour tout sommet t voisin du sommet s
#                si t n'est pas marqué
#                    p.empiler(t)

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
    for char, freq in sorted_counts:
        binary_tree = BinaryTree(char, freq)
        binary_trees.append(binary_tree)

    return sorted_counts



def insert_sorted(lst:list[BinaryTree], val:BinaryTree):
    index = 0
    while index < len(lst) and lst[index].freq >= val.freq:
        index += 1
    lst.insert(index, val)
    return lst