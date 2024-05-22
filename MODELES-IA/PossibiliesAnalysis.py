from itertools import  product, combinations

# 254 possibilities
def getAllPossibleWords(word_min =1,word_max=7):
    words =[]
    for i in range(word_min,word_max+1):
        productResults= (list( product([0,1],repeat=i)))
        for pr in productResults:
            words.append(''.join([str(element) for element in pr])) 
    return words

# 254!/(2!(254-2)!) + 254!/(3!(254-3)!) + 254!/(4!(254-4)!) + 254!/(5!(254-5)!) +
# 254!/(6!(254-6)!) + 254!/(7!(254-7)!) + 254!/(8!(254-8)!) + 254!/(9!(254-9)!) + 254!/(10!(254-10)!)

# 268 331 787 405 251 911 possibilities
def generatePossibilities(codePath ="C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/codeDatas.txt",
                          noCodePath="C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/notCodeDatas.txt",
                          lan_min =2 , lan_max=4,word_min =1,word_max=7):
    with open(codePath,'a') as codee , open(noCodePath) as notcodee:
        # generer toutes les possibilites pour les mots
        allWords = getAllPossibleWords(word_min,word_max)
        print(len(allWords))
        # ampiasaina amzay io liste io hi generer-na ny combinaisons rehetra
        # possible
        languages=[]
        for i in range(lan_min,lan_max+1):
            comb = list(combinations(allWords,i))
            print(len(comb))
            for combination in comb:
                oneElement = list(combination)
                languages.append(oneElement)
        return languages

