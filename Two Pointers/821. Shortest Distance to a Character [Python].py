class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        s_lst = []
        for i in range(len(s)):
            if s[i] == c:
                s_lst.append(i)

        ans = []
        j = 0
        
        for i in range(len(s)):
            if s[i] == c:
                j += 1
                ans.append(0)
            elif i < s_lst[0]:
                ans.append(s_lst[0]-i)
            elif i > s_lst[-1]:
                ans.append(i-s_lst[-1])
            else:
                ans.append(min(i-s_lst[j-1], s_lst[j]-i))
                
        return ans
