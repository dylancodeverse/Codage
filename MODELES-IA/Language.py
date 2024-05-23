
import SimilarityAnalysis
import ast
import time
import csv


class Language :
    def __init__(self , isCode, language:list[str]) -> None:
        self.isCode = isCode
        self.wordsLen = len(language)
        self.setZeroLen_OneLen(language) 
        self.setWordsWithSameSizeLen_TotalWordsSize(language)
        self.setTotalDiffRatio(language)
        self.setTotalDistancedeLevenshtein(language)
        self.setTotalSimilarityendstart(language)
        self.label = str(language)
        # ampiana kely hoe
        # self.set

    @staticmethod 
    def getHeader():
        return [   
                        "label",
                        "isCode",
                        "wordsLen",
                        "ZeroLen",
                        "OneLen",
                        "WordsWithSameSizeLen",
                        "TotalWordsSize",
                        "TotalDiffRatio",
                        "TotalDistancedeLevenshtein",
                        "TotalSimilarityendstart"
                    ]

    @staticmethod
    def exportDataAsCSV(
                             exportedCode ="C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/All/dataCode.csv"
                            ,exportedNotCode="C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/All/datanotCode.csv"
                            ,codePath="C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/NotPreparedTemp/codeDatas.txt"
                            ,notCodePath ="C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/NotPreparedTemp/notCodeDatas.txt"
                        ):

        fsec= (time.time())
        print('first step loading....')
        one ,two =Language.createLanguagesFromData(codePath, notCodePath)
        print(time.time()-fsec)
        lan = [one , two]
        print('data prepared')

        exp = [exportedCode, exportedNotCode ]

        for i in range(len(lan)) :
            header = Language.getHeader()
            fsec= (time.time())
            print('export csv....')
            with open(exp[i],'w',newline='') as filee:
                writer= csv.DictWriter(filee,fieldnames=header)
                writer.writeheader()
                for langg in lan [i] :
                    writer.writerow(
                    {
                        "label":langg.label
                        ,"isCode":langg.isCode
                        ,"wordsLen":langg.wordsLen
                        ,"ZeroLen":langg.zeroLen
                        ,"OneLen":langg.oneLen
                        ,"WordsWithSameSizeLen":langg.wordsWithSameSizeLen
                        ,"TotalWordsSize":langg.TotalWordsSize
                        ,"TotalDiffRatio":langg.TotalDiffRatio
                        ,"TotalDistancedeLevenshtein":langg.TotalDistancedeLevenshtein
                        ,"TotalSimilarityendstart":langg.TotalSimilarityendstart
                    })
            print(time.time()-fsec)


    @staticmethod
    def createTrainingDataAndPredictData(
                             codePath="C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/All/dataCode.csv"
                            ,notCodePath="C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/All/datanotCode.csv"
                            ,trainingDataPath = "C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/training/Training.csv"
                            ,predictDataPath = "C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/training/ToPredict.csv"
                        ):
        with open(codePath,'r') as codeFile , open(notCodePath,'r') as notCodeFile , open(trainingDataPath,'w') as trainingFile , open(predictDataPath,'w') as predictFile:
            codeLines =  codeFile.readlines()            
            notCodeLines = notCodeFile.readlines()

            trainingFile.writelines(codeLines[0:2501])
            trainingFile.writelines(notCodeLines[1:2501])

            predictFile.write(codeLines[0])
            predictFile.writelines(codeLines[2501:])
            predictFile.writelines(notCodeLines[2501:])


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
            listLanguageCodes.append(Language(1,code))
        for notCode in listNotCodes :
            listLanguageNotCodes.append(Language(0,notCode)) 
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

    def setWordsWithSameSizeLen_TotalWordsSize (self , language):
        self.wordsWithSameSizeLen = 0
        self.TotalWordsSize = 0
        sizeWord = []
        x = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0}
        for i in range(0,len(language)):
            leen =len(language[i])
            sizeWord.append(leen)
            x[str(leen)] +=1
        
        if x["1"] > 1 :
            self.wordsWithSameSizeLen += x["1"]
        if x["2"] > 1 :
            self.wordsWithSameSizeLen += x["2"]
        if x["3"] > 1 :
            self.wordsWithSameSizeLen += x["3"]
        if x["4"] > 1 :
            self.wordsWithSameSizeLen += x["4"]
        if x["5"] > 1 :
            self.wordsWithSameSizeLen += x["5"]
        if x["6"] > 1 :
            self.wordsWithSameSizeLen += x["6"]
        if x["7"] > 1 :
            self.wordsWithSameSizeLen += x["7"]


        self.TotalWordsSize = sum(sizeWord)            

    def setTotalDiffRatio(self,language ):
        self.TotalDiffRatio = SimilarityAnalysis.SimilarityAnalysis.getTotalRatio(language)

    def setTotalDistancedeLevenshtein(self,language ):
        self.TotalDistancedeLevenshtein = SimilarityAnalysis.SimilarityAnalysis.getTotalLevenshteinDistance(language)

    def setTotalSimilarityendstart(self,language ):
        self.TotalSimilarityendstart = SimilarityAnalysis.SimilarityAnalysis.getTotalprefix_suffix_similarity(language)



# Language.exportDataAsCSV()
Language.createTrainingDataAndPredictData()



