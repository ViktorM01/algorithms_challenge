class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix_arr = [0] * (n + 1)     
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = []

        for i in range(n):
            prefix_arr[i + 1] = prefix_arr[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix_arr[i + 1] += 1
 
        for q in queries:
            ans.append(prefix_arr[q[1] + 1] - prefix_arr[q[0]])
        
        return ans
