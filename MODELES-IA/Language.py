
import SimilarityAnalysis
import ast
import time
import csv


class Language :
    def __init__(self , isCode:bool, language:list[str]) -> None:
        self.isCode = isCode
        self.wordsLen = len(language)
        self.setZeroLen_OneLen(language) 
        self.setWordsWithSameSizeLen_AVGWordsSize(language)
        self.setAVGDiffRatio(language)
        self.setAVGDistancedeLevenshtein(language)
        self.setAVGSimilarityendstart(language)
        self.label = str(language)

    @staticmethod
    def exportDataAsCSV(exportedCode ,exportedNotCode , codePath,notCodePath):
        fsec= (time.time())
        print('first step loading....')
        one ,two =Language.createLanguagesFromData(codePath, notCodePath)
        print(time.time()-fsec)
        lan = [one , two]
        print('data prepared')

        exp = [exportedCode, exportedNotCode ]

        for i in range(len(lan)) :
            header =[   
                        "label",
                        "isCode",
                        "wordsLen",
                        "ZeroLen",
                        "OneLen",
                        "WordsWithSameSizeLen",
                        "AVGWordsSize",
                        "AVGDiffRatio",
                        "AVGDistancedeLevenshtein",
                        "AVGSimilarityendstart"
                    ]
            fsec= (time.time())
            print('export csv....')
            with open(exp[i],'w',newline='') as filee:
                writer= csv.DictWriter(filee,fieldnames=header)
                for langg in lan [i] :
                    writer.writerow(
                    {
                        "label":langg.label
                        ,"isCode":langg.isCode
                        ,"wordsLen":langg.wordsLen
                        ,"ZeroLen":langg.zeroLen
                        ,"OneLen":langg.oneLen
                        ,"WordsWithSameSizeLen":langg.wordsWithSameSizeLen
                        ,"AVGWordsSize":langg.AVGWordsSize
                        ,"AVGDiffRatio":langg.AVGDiffRatio
                        ,"AVGDistancedeLevenshtein":langg.AVGDistancedeLevenshtein
                        ,"AVGSimilarityendstart":langg.AVGSimilarityendstart
                    })
            print(time.time()-fsec)




    @staticmethod
    def createLanguagesFromData(codePath , notCodePath):
        listCodes =[]
        listNotCodes = []
        with open(codePath ,'r') as codeFile , open(notCodePath ,'r') as notCodeFile:
            for line in codeFile:
                lineList =ast.literal_eval(line.strip())
                listCodes.append(lineList)
            for line in notCodeFile :
                lineList =ast.literal_eval(line.strip())
                listNotCodes.append(lineList)
        listLanguageCodes = []
        listLanguageNotCodes = []
        for code in listCodes :
            listLanguageCodes.append(Language(True,code))
        for notCode in listNotCodes :
            listLanguageNotCodes.append(Language(False,notCode)) 
        return listLanguageCodes,listLanguageNotCodes            

    def setZeroLen_OneLen (self , language:list[str]):
        self.zeroLen =  0
        self.oneLen=0
        for element in language:        
            for letter in element:
                if letter =='0':
                    self.zeroLen += 1
                elif letter == '1':
                    self.oneLen+=1

    def setWordsWithSameSizeLen_AVGWordsSize (self , language):
        self.wordsWithSameSizeLen = 0
        self.AVGWordsSize = 0
        sizeWord = []
        for i in range(0,len(language)):
            sizeWord.append(len(language[i]))
            for j in range(i+1,len(language)):
                if len(language[i]) == len(language[j]):
                     self.wordsWithSameSizeLen+=1
        self.AVGWordsSize = sum(sizeWord)/len(language)            

    def setAVGDiffRatio(self,language ):
        self.AVGDiffRatio = SimilarityAnalysis.SimilarityAnalysis.getAVGRatio(language)

    def setAVGDistancedeLevenshtein(self,language ):
        self.AVGDistancedeLevenshtein = SimilarityAnalysis.SimilarityAnalysis.getAVGLevenshteinDistance(language)

    def setAVGSimilarityendstart(self,language ):
        self.AVGSimilarityendstart = SimilarityAnalysis.SimilarityAnalysis.getAVGprefix_suffix_similarity(language)


codePath = "C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/codeDatas.txt"
notCodePath = "C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/notCodeDatas.txt"
expcodePath = "C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/dataCode.csv"
expnotCodePath = "C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/datanotCode.csv"

Language.exportDataAsCSV(codePath=codePath ,exportedCode=expcodePath,exportedNotCode=expnotCodePath,notCodePath=notCodePath)



