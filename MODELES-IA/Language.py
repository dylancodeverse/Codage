
import SimilarityAnalysis

class Language :
    def __init__(self , isCode, language:list[str]) -> None:
        self.isCode = isCode
        self.wordsLen = len(language)
        self.setZeroLen_OneLen(self,language) 
        self.setWordsWithSameSizeLen_AVGWordsSize(self,language)
        self.setAVGDiffRatio(self,language)
        self.setAVGDistancedeLevenshtein(self,language)
        self.setAVGSimilarityendstart(self,language)

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
        self.ordsWithSameSizeLen = 0
        self.AVGWordsSize = 0
        sizeWord = []
        for i in range(0,len(language)):
            sizeWord.append(len(language[i]))
            for j in range(i+1,len(language)):
                if len(language[i]) == len(language[j]):
                     self.ordsWithSameSizeLen+=1
        self.AVGWordsSize = sum(sizeWord)/len(language)            

    def setAVGDiffRatio(self,language ):
        self.AVGDiffRatio = SimilarityAnalysis.SimilarityAnalysis.getAVGRatio(language)

    def setAVGDistancedeLevenshtein(self,language ):
        self.AVGDistancedeLevenshtein = SimilarityAnalysis.SimilarityAnalysis.getAVGLevenshteinDistance(language)

    def setAVGSimilarityendstart(self,language ):
        self.AVGSimilarityendstart = SimilarityAnalysis.SimilarityAnalysis.getAVGprefix_suffix_similarity(language)