import difflib
def similarite_chaine(str1, str2):
    ratio = difflib.SequenceMatcher(None, str1, str2).ratio()
    return ratio

# print(similarite_chaine('apple', 'applesauce'))


str1 = "apple"
str2 = "applesauce"

# diff = difflib.ndiff(str1, str2)
# print('\n'.join(diff))


str1 = "apple"
str2 = "applesauce"

# diff = difflib.unified_diff(str1, str2, lineterm='')
# print('\n'.join(diff))


import Levenshtein

str1 = "apple"
str2 = "applesauce"

# distance = Levenshtein.distance(str1, str2)
# print(f"Distance de Levenshtein : {distance}")


#  Longest Common Subsequence (LCS)
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L[m][n]

str1 = "10100"
str2 = "101011"

lcs_length = lcs(str1, str2)
print(f"Longueur de la plus longue sous-séquence commune : {lcs_length}")
