class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        char_lst = deque(['a', 'b', 'c'])
        ans_lst = []

        while char_lst:
            s = char_lst.popleft()
            if len(s) == n:
                ans_lst.append(s)
                continue
            for char in "abc":
                if s[-1] != char:
                    char_lst.append(s + char)
                    
        return "" if k > len(ans_lst) else ans_lst[k - 1]
