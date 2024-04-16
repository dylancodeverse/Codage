
class BinaryTree:
    def __init__(self,value,freq,leftChild=None, rightChild=None, parent=None) ->  None:
        self.value = value
        self.freq = freq
        self.leftChild = leftChild
        self.rightChild =rightChild
        self.parent = parent


def coding(message :str):
    # nodes ana prob miaraka amle caractere tries desc
    NodeDeProb = charcountDESC(message)
    nodesDone = []
    while NodeDeProb.count != 1:
        # jerena ny min anakiroa anle nodeDeProb
        min0 ,min1 = NodeDeProb[len(NodeDeProb)-2], NodeDeProb[len(NodeDeProb)-1]
        # mi former node vaovao as newNode
        newNode = BinaryTree(min0.value+min1.value,min0.freq+min1.freq,min1,min0)
        # ovaina ny parent anle min anakiroa
        min0.parent = newNode
        min1.parent = newNode
        # atsofoka anaty nodes ilay min anakiroa
        nodesDone.append(min0)
        nodesDone.append(min1)
        # fafana tao anaty nodedeprob ilay min anakiroa
        NodeDeProb= NodeDeProb[:-2]
        # ezahina atsofoka ao anaty ilay list nodeDeProb ilay node vaovao
        pass


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



def insert_sorted(lst, val):
    index = 0
    while index < len(lst) and lst[index] >= val:
        index += 1
    lst.insert(index, val)