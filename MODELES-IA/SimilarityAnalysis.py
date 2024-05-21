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

    @staticmethod
    def getAVGLevenshteinDistance(strings :list[str]):
        """
            calcul de LevenshteinDistance moyenne pour une liste de string
        """
        listLevenshteinDistance =[]
        for i in range(0,len(strings)) :
            for j in range (i+1,len(strings)):
                listLevenshteinDistance.append(SimilarityAnalysis.getLevenshteinDistance(strings[i],strings[j]))
        return sum(listLevenshteinDistance) / len(listLevenshteinDistance)


    @staticmethod 
    def LCS_prefix_suffix(str1:str, str2:str) -> int:
        """
        La plus longue sous-séquence commune prefix suffix est une mesure 
        de la similarité entre deux chaînes en trouvant 
        la plus longue séquence de caractères qui apparaît dans 
        les deux chaînes dans le même ordre, en tant que préfixe 
        ou suffixe dans chaque chaîne.
        (implementation specifique)
        """
        # etude du prefixe de str2
        cumulPrefixStr1PrefixStr2= ''
        for a in str2 :
            if str1.startswith(cumulPrefixStr1PrefixStr2+a):
                cumulPrefixStr1PrefixStr2+=cumulPrefixStr1PrefixStr2+a
            else:
                break                
        cumulSuffixStr1PrefixStr2= ''
        for a in str2 :
            if str1.endswith(cumulSuffixStr1PrefixStr2+a):
                cumulSuffixStr1PrefixStr2+=cumulSuffixStr1PrefixStr2+a
            else:
                break
        # etude du suffixe de str2
        reversedStr2 =  str2[::-1]            
        
        cumulPrefixStr1SuffixStr2= ''

                    






# Exemple d'utilisation
str1 = "abcdef"
str2 = "cdefgh"
resultat = SimilarityAnalysis.LCS_prefix_suffix(str1, str2)
print("Longest Common Subsequence (Prefix and Suffix):", resultat)