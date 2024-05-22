import random
import sys
sys.path.append("c:/Users/MISA/Desktop/Workspace/S6/Codage")
import Programmes.SardinasPaterson.SardinasPaterson as  SardinasPaterson
from itertools import  product, combinations

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

# 268 331 787 405 251 911 possibilities
# def generatePossibilities(codePath ="C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/codeDatas.txt",
#                           noCodePath="C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/notCodeDatas.txt",
#                           lan_min =2 , lan_max=4,word_min =1,word_max=7):
#     with open(codePath,'a') as codee , open(noCodePath) as notcodee:
#         # generer toutes les possibilites pour les mots
#         allWords = getAllPossibleWords(word_min,word_max)
#         print(len(allWords))
#         # ampiasaina amzay io liste io hi generer-na ny combinaisons rehetra
#         # possible
#         languages=[]
#         for i in range(lan_min,lan_max+1):
#             comb = list(combinations(allWords,i))
#             print(len(comb))
#             for combination in comb:
#                 oneElement = list(combination)
#                 languages.append(oneElement)
#         return languages

def getAllPossibleWords(word_min =1,word_max=7):
    words =[]
    for i in range(word_min,word_max+1):
        productResults= (list( product([0,1],repeat=i)))
        for pr in productResults:
            words.append(''.join([str(element) for element in pr])) 
    return words

generatePossibilities()

# 254!/(2!(254-2)!) + 254!/(3!(254-3)!) + 254!/(4!(254-4)!) + 254!/(5!(254-5)!) +
# 254!/(6!(254-6)!) + 254!/(7!(254-7)!) + 254!/(8!(254-8)!) + 254!/(9!(254-9)!) + 254!/(10!(254-10)!)