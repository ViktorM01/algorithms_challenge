class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        i = 0
        lst = []

        while i < n:
            start = i
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            if i == start:
                lst.append(str(nums[start]))
            else:
                lst.append(f'{nums[start]}->{nums[i]}')
            i += 1

        return lst
