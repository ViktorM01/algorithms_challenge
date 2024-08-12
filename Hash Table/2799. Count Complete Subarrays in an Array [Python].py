class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n, distinct = len(nums), len(set(nums))
        l, r, count = 0, 0, 0
        counter = Counter()

        while r < n: 
            counter[nums[r]] += 1
            while distinct == len(counter):
                counter[nums[l]] -= 1
                if counter[nums[l]] == 0:
                    del counter[nums[l]]
                l += 1
                count += n - r
            r += 1
        
        return count
