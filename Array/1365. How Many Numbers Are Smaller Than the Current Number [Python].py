class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        nums_sort = sorted(nums)
        map_dict, flst = dict(), list()

        for i in range(len(nums_sort)):
            if nums_sort[i] not in map_dict:
                map_dict[nums_sort[i]] = i
        for i in range(len(nums)):
            flst.append(map_dict[nums[i]])
            
        return flst
