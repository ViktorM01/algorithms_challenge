class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        std::vector<int> lst(nums.size());
        int l = 0;
        int r = nums.size() - 1;
        for (int i = nums.size() - 1; i >= 0; --i) {
            if (l <= r) {
                if (std::abs(nums[l]) >= std::abs(nums[r])) {
                    lst[i] = nums[l] * nums[l];
                    ++l;
                } else {
                    lst[i] = nums[r] * nums[r];
                    --r;
                }
            }
        }
        return lst;
    }
};
