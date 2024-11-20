class Solution:
    def takeCharacters(self, text: str, req: int) -> int:
        freq = [0] * 3
        size = len(text)
        
        for char in text:
            freq[ord(char) - ord('a')] += 1
        
        l, r = 0, 0
        
        if freq[0] < req or freq[1] < req or freq[2] < req:
            return -1
        
        for r in range(size):
            freq[ord(text[r]) - ord('a')] -= 1
            
            if freq[0] < req or freq[1] < req or freq[2] < req:
                freq[ord(text[l]) - ord('a')] += 1
                l += 1
        
        return size - (r - l + 1)
