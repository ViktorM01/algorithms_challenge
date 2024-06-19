class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()
        while l <= r:
            while l <= r and not s[l].isalnum():
                l += 1
            while l <= r and not s[r].isalnum():
                r -= 1
            if l <= r and s[l] == s[r]:
                l += 1
                r -= 1
            else:
                break
        if l < r:
            return False
        return True
