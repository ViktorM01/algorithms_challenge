class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        lst1, lst2 = str(), str()
        for i in word1:
            lst1 = lst1 + i
        for j in word2:
            lst2 = lst2 + j
        return lst1 == lst2
