class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False

        # first traverse for open brackets
        bracket, changes = 0, 0
        for i in range(n):
            if locked[i] == '0':
                changes += 1
            else:
                if s[i] == '(':
                    bracket += 1
                else:
                    bracket -= 1
            if changes + bracket < 0:
                return False

        # second traverse for close brackets
        bracket, changes = 0, 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '0':
                changes += 1
            else:
                if s[i] == ')':
                    bracket += 1
                else:
                    bracket -= 1
            if changes + bracket < 0:
                return False

        return True
