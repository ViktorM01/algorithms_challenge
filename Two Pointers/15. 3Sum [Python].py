class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = []

        for i in range(len(nums)):
            if i > 0  and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ > 0:
                    k -= 1
                elif sum_ < 0:
                    j += 1
                else:
                    lst.append([nums[i], nums[j], nums[k]])
                    j += 1
                
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return lst
