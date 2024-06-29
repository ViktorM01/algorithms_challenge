rewrite in C++ 


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lst = []
        row1, row2, row3 = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        for i in words:
            len_word = set(i.lower())
            c = max(len(set(row1) & len_word), len(set(row2) & len_word), len(set(row3) & len_word))
            if c == len(len_word):
                 lst.append(i)
        return lst
