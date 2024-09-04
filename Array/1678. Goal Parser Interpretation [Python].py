class Solution:
    def interpret(self, command: str) -> str:
        lst = []
        for i in range(len(command)):
            if command[i] == 'G':
                lst.append('G')
            elif command[i] == '(' and command[i+1] == ')':
                lst.append('o')
            elif command[i] == '(' and command[i+1] == 'a':
                lst.append('al')
        return ''.join(lst)
