class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_val = 0
        for i in sentences:
            max_val = max(len(i.split()), max_val)
        return max_val
