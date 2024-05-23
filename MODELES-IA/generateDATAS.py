import random
import sys
import time
sys.path.append("c:/Users/MISA/Desktop/Workspace/S6/Codage")
from Programmes.SardinasPaterson.SardinasPaterson  import SardinasPaterson as sardina

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

# print(list(generateLanguage()))

def generateNLanguages(
        codePath = "C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/NotPreparedTemp/codeDatas.txt",
        notCodePath = "C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/NotPreparedTemp/notCodeDatas.txt",
        size = 100000 ):
    code = []
    notCode = []
    with open(codePath ,'w') as codeFile , open(notCodePath ,'w') as notCodeFile:
        i = 0
        while len(code)+len(notCode)!=size :
            language = list( generateLanguage())
            if sardina.estCeUnCode(language):
                if language not in code:
                    if len(language)==2 and i <500:
                        i+=1
                        code.append(language)
                        codeFile.write(str(language)+'\n')
                    elif len(language)!=2 :                    
                        code.append(language)
                        codeFile.write(str(language)+'\n')
            else :
                if language not in notCode:
                    notCode.append(language)           
                    notCodeFile.write(str(language)+'\n')
            print(len(code)+len(notCode))                     
        return code ,notCode
 
timesf = time.time()
code , notcode= generateNLanguages() 
print(str(time.time()-timesf)+'second')
# print (len(code) )
# print(len(notcode))
    



