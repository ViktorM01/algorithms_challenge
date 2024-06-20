class Solution:
    def romanToInt(self, s: str) -> int:
            calc = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

            f_sum = 0

            for i in range(len(s)):
                if i < len(s) - 1 and calc[s[i]] < calc[s[i+1]]:
                    f_sum -= calc[s[i]]
                else:
                    f_sum += calc[s[i]]
            
            return f_sum
