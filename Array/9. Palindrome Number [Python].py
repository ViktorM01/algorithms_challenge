class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        str_s = str(x)
        len_s = len(str_s)

        for i in range(len_s >> 1):
            if str_s[i] != str_s[len_s - 1 - i]:
                return False
        
        return True
