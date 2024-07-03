class Solution {
public:
    int minDifference(vector<int>& nums) {
        int n = nums.size();
        if (n <= 4) {
            return 0;
        }
        std::sort(nums.begin(), nums.end());
        int min_diff = nums[n - 1] - nums[0];
        for (int i = 0; i < 4; ++i) {
            min_diff = std::min(min_diff, nums[n - 4 + i] - nums[i]);
        }
        return min_diff;
    }
};
