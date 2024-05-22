import random
import sys
sys.path.append("c:/Users/MISA/Desktop/Workspace/S6/Codage")
import Programmes.SardinasPaterson.SardinasPaterson as  SardinasPaterson

# 254 possibilites
def generateBinaryWord(min_length=1, max_length=7):
    # Tokony fantarina alony hoe firy lay alavany
    size = random.randint(min_length, max_length)
    response = ''
    for i in range(size):
        response += str(random.randint(0, 1))
    return response

def generateLanguage(lan_min =1 , lan_max=10,word_min =1,word_max=7):
    # Tokony fantarina tsotra hoe anakifiry lay word generer-na
    size = random.randint(lan_min, lan_max)
    # avy eo antsoina ilay generateBinaryWord ahafahana mi creer langage
    # set amzay mba tena ensemble tokoa lay resaka
    setofwords = set()
    while len(setofwords)!=size :
        setofwords.add(generateBinaryWord(word_min,word_max)) 
    # averina en tant que liste
    return setofwords 

print(list(generateLanguage()))

def generateNLanguages(size = 5000 ):
    code = set()
    notCode = set()
    while len(code)+len(notCode)!=size :
        language = generateLanguage()




