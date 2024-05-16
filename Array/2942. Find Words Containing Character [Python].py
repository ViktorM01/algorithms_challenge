class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        lst = []
        
        for el in range(len(words)):
            if x in words[el]:
                lst.append(el)

        return lst
