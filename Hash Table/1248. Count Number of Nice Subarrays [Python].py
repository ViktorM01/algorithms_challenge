class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.at_most(nums, k) - self.at_most(nums, k - 1)

    def at_most(self, nums: List[int], k: int) -> int:
        wdw_size, subarr, start = 0, 0, 0
        for end in range(len(nums)):
            wdw_size += nums[end] % 2
            while wdw_size > k:
                wdw_size -= nums[start] % 2
                start += 1
            subarr += end - start + 1
        return subarr
