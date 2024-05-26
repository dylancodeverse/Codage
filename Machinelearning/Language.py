import sys
sys.path.append("C:/Users/MISA/Desktop/Workspace/S6/Python/Codage")
import analysis.SimilarityAnalysis as SimilarityAnalysis
import ast
import time
import csv
import Programmes.OperationNombre.BaseToBase as B
import joblib
import numpy as np
class Language :
    def __init__(self , isCode, language:list[str]) -> None:
        self.isCode = isCode
        self.wordsLen = len(language)
        self.setZeroLen_OneLen(language) 
        self.setWordsWithSameSizeLen_TotalWordsSize(language)
        self.setTotalDiffRatio(language)
        self.setTotalDistancedeLevenshtein(language)
        self.setTotalSimilarityendstart(language)
        self.setIsLongueurFixe(language)
        self.label = str(language)
        self.setRepresentationEnBase10(language)
        # ampiana kely hoe
        # self.set
    def predict(self,modelPath='C:/Users/MISA/Desktop/Workspace/S6/Python/Codage/Machinelearning/randomforestModel/Predict.joblib'):
        model = joblib.load(modelPath)
        datas =np.array([[self.wordsLen,self.zeroLen,self.oneLen,self.wordsWithSameSizeLen,self.TotalWordsSize,self.TotalDiffRatio,self.TotalDistancedeLevenshtein,self.TotalSimilarityendstart,self.isLongueurFixe,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine,self.ten,self.coloneLen,self.coltwoLen,self.colthreeLen,self.colfourLen,self.colfiveLen,self.colsixLen,self.colsevenLen,self.coleightLen,self.colnineLen,self.coltenLen,self.coloneZeroFreq,self.coloneOneFreq,self.coltwoZeroFreq,self.coltwoOneFreq,self.colthrZeroFreq,self.colthrOneFreq,self.colfouZeroFreq,self.colfouOneFreq,self.colfivZeroFreq,self.colfivOneFreq,self.colsixZeroFreq,self.colsixOneFreq,self.colsevZeroFreq,self.colsevOneFreq,self.coleigZeroFreq,self.coleigOneFreq,self.colninZeroFreq,self.colninOneFreq,self.coltenZeroFreq,self.coltenOneFreq]])
        print(datas)
        return model.predict(datas)

    @staticmethod 
    def getHeader():
        return [   
                        "label"
                        ,"isCode"
                        ,"wordsLen"
                        ,"ZeroLen"
                        ,"OneLen"
                        ,"WordsWithSameSizeLen"
                        ,"TotalWordsSize"
                        ,"TotalDiffRatio"
                        ,"TotalDistancedeLevenshtein"
                        ,"TotalSimilarityendstart"
                        ,"isLongueurFixe"
                        ,"one"
                        ,"two"
                        ,"three"
                        ,"four"
                        ,"five"
                        ,"six"
                        ,"seven"
                        ,"eight"
                        ,"nine"
                        ,"ten"
                        ,"coloneLen"
                        ,"coltwoLen"
                        ,"colthreeLen"
                        ,"colfourLen"
                        ,"colfiveLen"
                        ,"colsixLen"
                        ,"colsevenLen"
                        ,"coleightLen"
                        ,"colnineLen"
                        ,"coltenLen"
                        ,"coloneZeroFreq"
                        ,"coloneOneFreq" 
                        ,"coltwoZeroFreq"
                        ,"coltwoOneFreq" 
                        ,"colthrZeroFreq"
                        ,"colthrOneFreq" 
                        ,"colfouZeroFreq"
                        ,"colfouOneFreq" 
                        ,"colfivZeroFreq"
                        ,"colfivOneFreq" 
                        ,"colsixZeroFreq"
                        ,"colsixOneFreq" 
                        ,"colsevZeroFreq"
                        ,"colsevOneFreq" 
                        ,"coleigZeroFreq"
                        ,"coleigOneFreq" 
                        ,"colninZeroFreq"
                        ,"colninOneFreq" 
                        ,"coltenZeroFreq"
                        ,"coltenOneFreq"                         
                    ]

    @staticmethod
    def exportDataAsCSV(
                             exportedCode ="C:/Users/MISA/Desktop/Workspace/S6/Python/Codage/Machinelearning/datas/All/dataCode.csv"
                            ,exportedNotCode="C:/Users/MISA/Desktop/Workspace/S6/Python/Codage/Machinelearning/datas/All/datanotCode.csv"
                            ,codePath="C:/Users/MISA/Desktop/Workspace/S6/Python/Codage/Machinelearning/datas/NotPreparedTemp/codeDatas.txt"
                            ,notCodePath ="C:/Users/MISA/Desktop/Workspace/S6/Python/Codage/Machinelearning/datas/NotPreparedTemp/notCodeDatas.txt"
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
                        ,"isLongueurFixe":langg.isLongueurFixe
                        ,"one":langg.one
                        ,"two":langg.two
                        ,"three":langg.three
                        ,"four":langg.four
                        ,"five":langg.five
                        ,"six":langg.six
                        ,"seven":langg.seven
                        ,"eight":langg.eight
                        ,"nine":langg.nine
                        ,"ten":langg.ten
                        ,"coloneLen":langg.coloneLen
                        ,"coltwoLen":langg.coltwoLen
                        ,"colthreeLen":langg.colthreeLen
                        ,"colfourLen":langg.colfourLen
                        ,"colfiveLen":langg.colfiveLen
                        ,"colsixLen":langg.colsixLen
                        ,"colsevenLen":langg.colsevenLen
                        ,"coleightLen":langg.coleightLen
                        ,"colnineLen":langg.colnineLen
                        ,"coltenLen":langg.coltenLen                        
                        ,"coloneZeroFreq":langg.coloneZeroFreq
                        ,"coloneOneFreq":langg.coloneOneFreq 
                        ,"coltwoZeroFreq":langg.coltwoZeroFreq
                        ,"coltwoOneFreq":langg.coltwoOneFreq 
                        ,"colthrZeroFreq":langg.colthrZeroFreq
                        ,"colthrOneFreq":langg.colthrOneFreq 
                        ,"colfouZeroFreq":langg.colfouZeroFreq
                        ,"colfouOneFreq":langg.colfouOneFreq 
                        ,"colfivZeroFreq":langg.colfivZeroFreq
                        ,"colfivOneFreq":langg.colfivOneFreq 
                        ,"colsixZeroFreq":langg.colsixZeroFreq
                        ,"colsixOneFreq":langg.colsixOneFreq 
                        ,"colsevZeroFreq":langg.colsevZeroFreq
                        ,"colsevOneFreq":langg.colsevOneFreq 
                        ,"coleigZeroFreq":langg.coleigZeroFreq
                        ,"coleigOneFreq":langg.coleigOneFreq 
                        ,"colninZeroFreq":langg.colninZeroFreq
                        ,"colninOneFreq":langg.colninOneFreq 
                        ,"coltenZeroFreq":langg.coltenZeroFreq
                        ,"coltenOneFreq":langg.coltenOneFreq            
                    })
            print(time.time()-fsec)


    @staticmethod
    def createTrainingDataAndPredictData(
                             codePath="C:/Users/MISA/Desktop/Workspace/S6/Python/Codage/Machinelearning/datas/All/dataCode.csv"
                            ,notCodePath="C:/Users/MISA/Desktop/Workspace/S6/Python/Codage/Machinelearning/datas/All/datanotCode.csv"
                            ,trainingDataPath = "C:/Users/MISA/Desktop/Workspace/S6/Python/Codage/Machinelearning/datas/training/Training.csv"
                            ,predictDataPath = "C:/Users/MISA/Desktop/Workspace/S6/Python/Codage/Machinelearning/datas/training/ToPredict.csv"
                        ):
        with open(codePath,'r') as codeFile , open(notCodePath,'r') as notCodeFile , open(trainingDataPath,'w') as trainingFile , open(predictDataPath,'w') as predictFile:
            codeLines =  codeFile.readlines()            
            notCodeLines = notCodeFile.readlines()
            trainingFile.writelines(codeLines[0:251])
            trainingFile.writelines(codeLines[501:2751])
            trainingFile.writelines(notCodeLines[1:2501])

            predictFile.write(codeLines[0])
            predictFile.writelines(codeLines[251:501])
            predictFile.writelines(codeLines[2751:])
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

    def setIsLongueurFixe(self,language):
        oneLen = len(language[0])
        for element in language[1:]:
            if oneLen != len(element):
                self.isLongueurFixe = 0
                return
        self.isLongueurFixe =1
    def setRepresentationEnBase10(self,language):
        self.one = B.enBase10( language[0] ,2,None)
        self.coloneLen = len(language[0])
        self.coloneZeroFreq,self.coloneOneFreq=SimilarityAnalysis.SimilarityAnalysis.getZeroLen_OneLen(language[0])
        self.two=0
        self.coltwoLen=0
        self.coltwoOneFreq=0
        self.coltwoZeroFreq=0
        self.three=0
        self.colthreeLen=0
        self.colthrOneFreq=0
        self.colthrZeroFreq=0
        self.four=0
        self.colfourLen=0
        self.colfouOneFreq=0
        self.colfouZeroFreq=0
        self.five=0
        self.colfiveLen=0
        self.colfivOneFreq=0
        self.colfivZeroFreq=0
        self.six=0
        self.colsixLen=0
        self.colsixOneFreq=0
        self.colsixZeroFreq=0
        self.seven=0
        self.colsevenLen=0
        self.colsevOneFreq=0
        self.colsevZeroFreq=0
        self.eight=0
        self.coleightLen=0
        self.coleigOneFreq=0
        self.coleigZeroFreq=0
        self.nine=0
        self.colnineLen=0
        self.colninOneFreq=0
        self.colninZeroFreq=0
        self.ten=0
        self.coltenLen=0
        self.coltenOneFreq=0
        self.coltenZeroFreq=0
        if len(language) >1:
            self.two = B.enBase10( language[1] ,2,None)
            self.coltwoLen=len(language[1])
            self.coltwoZeroFreq,self.coltwoOneFreq = SimilarityAnalysis.SimilarityAnalysis.getZeroLen_OneLen(language[1])
        if len (language) >2:
            self.three = B.enBase10( language[2] ,2,None)
            self.colthreeLen=len(language[2])
            self.colthrZeroFreq,self.colthrOneFreq = SimilarityAnalysis.SimilarityAnalysis.getZeroLen_OneLen(language[2])
        if len (language) >3:
            self.four = B.enBase10( language[3] ,2,None)
            self.colfourLen=len(language[3])
            self.colfouZeroFreq,self.colfouOneFreq = SimilarityAnalysis.SimilarityAnalysis.getZeroLen_OneLen(language[3])
        if len (language) >4:
            self.five = B.enBase10( language[4] ,2,None)
            self.colfiveLen=len(language[4])
            self.colfivZeroFreq,self.colfivOneFreq = SimilarityAnalysis.SimilarityAnalysis.getZeroLen_OneLen(language[4])
        if len (language) >5:
            self.six = B.enBase10( language[5] ,2,None)
            self.colsixLen=len(language[5])
            self.colsixZeroFreq,self.colsixOneFreq = SimilarityAnalysis.SimilarityAnalysis.getZeroLen_OneLen(language[5])
        if len (language) >6:
            self.seven = B.enBase10( language[6] ,2,None)
            self.colsevenLen=len(language[6])
            self.colsevZeroFreq,self.colsevOneFreq = SimilarityAnalysis.SimilarityAnalysis.getZeroLen_OneLen(language[6])
        if len (language) >7:
            self.eight = B.enBase10( language[7] ,2,None)
            self.coleightLen=len(language[7])
            self.coleigZeroFreq,self.coleigOneFreq = SimilarityAnalysis.SimilarityAnalysis.getZeroLen_OneLen(language[7])
        if len (language) >8:
            self.nine = B.enBase10( language[8] ,2,None)
            self.colnineLen=len(language[8])
            self.colninZeroFreq,self.colninOneFreq = SimilarityAnalysis.SimilarityAnalysis.getZeroLen_OneLen(language[8])
        if len (language) >9:
            self.ten = B.enBase10( language[9] ,2,None)
            self.coltenLen=len(language[9])
            self.coltenZeroFreq,self.coltenOneFreq = SimilarityAnalysis.SimilarityAnalysis.getZeroLen_OneLen(language[9])



# Language.exportDataAsCSV()
# print( Language.createTrainingDataAndPredictData())

import Programmes.SardinasPaterson.SardinasPaterson as sardina

test = ['101','010','10']
print( Language(None,test).predict()[0]==1)
print(sardina.SardinasPaterson.estCeUnCode(test))
# 10 101 010
# 101 01 010