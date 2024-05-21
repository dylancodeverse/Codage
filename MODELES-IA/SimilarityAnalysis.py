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
        return sum(listRatio) / len(listRatio)

    @staticmethod 
    def getLevenshteinDistance(str1, str2)->int:
        return Levenshtein.distance(str1, str2)


    #  Longest Common Subsequence (LCS)
    @staticmethod 
    def LCS(str1 ,str2) -> int :
        """
        La plus longue sous-séquence commune est une mesure 
        de la similarité entre deux chaînes en trouvant 
        la plus longue séquence de caractères qui apparaît dans 
        les deux chaînes dans le même ordre.
        """
        m = len(str1)
        n = len(str2)
        L = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif str1[i - 1] == str2[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])
        return L[m][n]
    