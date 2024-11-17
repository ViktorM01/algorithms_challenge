class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst = []

        def dfs(left_p, right_p, s):
            if left_p == right_p and left_p + right_p == n * 2:
                lst.append(s)
                return
            
            if left_p < n:
                dfs(left_p + 1, right_p, s + '(')
            if right_p < left_p:
                dfs(left_p, right_p + 1, s + ')')

        dfs(0, 0, "")

        return lst
