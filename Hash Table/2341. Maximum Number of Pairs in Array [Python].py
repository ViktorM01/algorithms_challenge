class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs, pr_new = 0, 0
        dic = {key: nums.count(key) for key in set(nums)}
        for k in dic.keys():
            pr_new += dic[k] // 2
            pairs += pr_new
            dic[k] -= pr_new * 2
            pr_new = 0
        return [pairs, sum(dic.values())]
