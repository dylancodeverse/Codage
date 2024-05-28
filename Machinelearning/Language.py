import sys
sys.path.append("C:/Users/MISA/Desktop/Workspace/S6/Python/Codage")
import Machinelearning.analysis.SimilarityAnalysis as SimilarityAnalysis
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
        # self.setKraftMcMilanSatisfied(language)
        self.setplusLongueSimilitudeRatioPlusieurs(language)
        # ampiana kely hoe
        # self.set
    def predict(self,modelPath='C:/Users/MISA/Desktop/Workspace/S6/Python/Codage/Machinelearning/randomforestModel/Predict.joblib'):
        model = joblib.load(modelPath)
        datas =np.array([self.values()[2:]])
        print(datas)
        # print(datas)
        return model.predict(datas)

    @staticmethod 
    def getHeader():
        return [   
                        "label"
                        ,"isCode"
                        ,"wordsLen"
                        ,"ZeroLen"
                        ,"OneLen"
                        ,"TotalWordsSize"
                        ,"TotalDiffRatio"
                        ,"TotalDistancedeLevenshtein"
                        ,"TotalSimilarityendstart"
                        ,"isLongueurFixe"
                        # ,"kraftMcMilanSatisfied"
                        ,"WordsWithSameSizeLen"
                        ,"plusLongueSimilitudeRatioPlusieurs"
                    ]
    def dictValues (self):
        return {
                        "label":self.label
                        ,"isCode":self.isCode
                        ,"wordsLen":self.wordsLen
                        ,"ZeroLen":self.zeroLen
                        ,"OneLen":self.oneLen
                        ,"TotalWordsSize":self.TotalWordsSize
                        ,"TotalDiffRatio":self.TotalDiffRatio
                        ,"TotalDistancedeLevenshtein":self.TotalDistancedeLevenshtein
                        ,"TotalSimilarityendstart":self.TotalSimilarityendstart
                        ,"isLongueurFixe":self.isLongueurFixe
                        # ,"kraftMcMilanSatisfied":self.kraftMcMilanSatisfied
                        ,"WordsWithSameSizeLen":self.wordsWithSameSizeLen
                        ,"plusLongueSimilitudeRatioPlusieurs":self.plusLongueSimilitudeRatioPlusieurs
                    }

    def values(self):
        return [self.label ,self.isCode, self.wordsLen,
                self.zeroLen , self.oneLen ,
                self.TotalWordsSize ,self.TotalDiffRatio,
                self.TotalDistancedeLevenshtein,
                self.TotalSimilarityendstart, 
                self.isLongueurFixe,
                # self.kraftMcMilanSatisfied,
                self.wordsWithSameSizeLen
                ,self.plusLongueSimilitudeRatioPlusieurs
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
                    writer.writerow(langg.dictValues())
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
    def createLanguagesFromData(codePath , notCodePath) :
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

    def setplusLongueSimilitudeRatioPlusieurs(self,language):
        self.plusLongueSimilitudeRatioPlusieurs = SimilarityAnalysis.SimilarityAnalysis.plusLongueSimilitudeRatioPlusieurs(language)

    def setIsLongueurFixe(self,language):
        oneLen = len(language[0])
        for element in language[1:]:
            if oneLen != len(element):
                self.isLongueurFixe = 0
                return
        self.isLongueurFixe =1

    def setKraftMcMilanSatisfied(self,language):
        summ = 0
        for element in language:
            summ+=2**-len(element)
        if summ <=1:
            self.kraftMcMilanSatisfied = 1
        else:
            self.kraftMcMilanSatisfied = 0



# import Programmes.SardinasPaterson.SardinasPaterson as sardina

# test = ['101','010','10']
# print( Language(None,test).predict()[0]==1)
# print(sardina.SardinasPaterson.estCeUnCode(test))
# 10 101 010
# 101 01 010