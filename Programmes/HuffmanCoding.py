def coding(message :str):
    tableauDeProb = charcount(message)


    pass

def charcount(message:str)->dict:
    counts = {}
    for char in message:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts




class BinaryTree:
    def __init__(self,value,freq,leftChild:'BinaryTree',rightChild:'BinaryTree',parent:'BinaryTree') -> None:
        self.value = value
        self.freq = freq
        self.leftChild = leftChild
        self.rightChild =rightChild
        self.parent = parent