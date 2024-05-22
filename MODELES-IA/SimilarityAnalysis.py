import difflib
# pip install python-Levenshtein
import Levenshtein



class SimilarityAnalysis:
     
    @staticmethod 
    def getRatio(str1, str2)->float:
        """
            Le ratio de similarité est un nombre entre 
            0 et 1 où 1 signifie que les chaînes sont
            identiques et 0 signifie qu'elles sont complètement 
            différentes.
        """
        return difflib.SequenceMatcher(None, str1, str2).ratio()
    
    @staticmethod 
    def getAVGRatio(strings :list[str]):
        """
            calcul de ratio moyenne pour une liste de string
        """
        listRatio =[]
        for i in range(0,len(strings)) :
            for j in range (i+1,len(strings)):
                listRatio.append(SimilarityAnalysis.getRatio(strings[i],strings[j]))
        if (len(listRatio)==0):
            return 0                
        return sum(listRatio) / len(listRatio)

    @staticmethod 
    def getLevenshteinDistance(str1, str2)->int:
        return Levenshtein.distance(str1, str2)

    @staticmethod
    def getAVGLevenshteinDistance(strings :list[str]):
        """
            calcul de LevenshteinDistance moyenne pour une liste de string
        """
        listLevenshteinDistance =[]
        for i in range(0,len(strings)) :
            for j in range (i+1,len(strings)):
                listLevenshteinDistance.append(SimilarityAnalysis.getLevenshteinDistance(strings[i],strings[j]))
        if (len(listLevenshteinDistance)==0):
            return 0                 
        return sum(listLevenshteinDistance) / len(listLevenshteinDistance)


    @staticmethod 
    def prefix_suffix_similarity(str1:str, str2:str) -> int:
        """
        Noter la similitude entre les bouts des deux strings.
        (implementation specifique)
        """
        if (str1== str2) :
            return len(str1)

        # etude du prefixe de str2
        cumulPrefixStr1PrefixStr2= ''
        for a in str2 :
            if str1.startswith(cumulPrefixStr1PrefixStr2+a):
                cumulPrefixStr1PrefixStr2+=a
            else:
                break                
        cumulSuffixStr1PrefixStr2= ''
        for a in str2 :
            if str1.endswith(cumulSuffixStr1PrefixStr2+a):
                cumulSuffixStr1PrefixStr2+=a
            else:
                break
        # etude du suffixe de str2
        reversedStr2 =  str2[::-1]            
        cumulPrefixStr1SuffixStr2= ''
        for a in reversedStr2 :
            if str1.startswith(a+ cumulPrefixStr1SuffixStr2):
                cumulPrefixStr1SuffixStr2=a+cumulPrefixStr1SuffixStr2
            else:
                break      
        cumulSuffixStr1SuffixStr2= ''                
        for a in reversedStr2 :
            if str1.endswith(a+cumulSuffixStr1SuffixStr2):
                cumulSuffixStr1SuffixStr2=a+cumulSuffixStr1SuffixStr2
            else:
                break                      
        return len(cumulPrefixStr1PrefixStr2)+len(cumulSuffixStr1PrefixStr2)+ len(cumulPrefixStr1SuffixStr2) + len(cumulSuffixStr1SuffixStr2)                 

                    
    @staticmethod
    def getAVGprefix_suffix_similarity(strings :list[str]):
        """
            calcul de prefix_suffix_similarity moyenne pour une liste de string
        """
        prefixsuffixsimilaritynote =[]
        for i in range(0,len(strings)) :
            for j in range (i+1,len(strings)):
                prefixsuffixsimilaritynote.append(SimilarityAnalysis.prefix_suffix_similarity(strings[i],strings[j]))
        if (len(prefixsuffixsimilaritynote)==0):
            return 0                 
        return sum(prefixsuffixsimilaritynote) / len(prefixsuffixsimilaritynote)

    
    @staticmethod
    def getFrequency(strings:list[str],string):
        frequence = 0
        for x in strings:
            for a in x :
                if a == string:
                    frequence+=1
        return frequence
    @staticmethod
    def getNWordWithSameSize(strings:list[str]):
        n = 0
        for i in range(0,len(strings)) :
            for j in range (i+1,len(strings)):
                if len(strings[i]) == len (strings[j]):
                    n+=1
        return 1




