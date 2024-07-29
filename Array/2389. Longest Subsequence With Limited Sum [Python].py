class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answers = []
        nums.sort()
        n = len(nums)
        
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        def bin_search(arr, target):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                num = arr[mid]
                if num > target:
                    r = mid - 1
                else: 
                    l = mid + 1
            return l
        
        for i in queries:
            answers.append(bin_search(prefix_sum, i))
            
        return answers
