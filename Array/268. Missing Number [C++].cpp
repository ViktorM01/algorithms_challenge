class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int abs_s = (n * (n + 1)) / 2;
        return abs_s - accumulate(nums.begin(), nums.end(), 0);
    }
};
