class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int p1 = 0;
        int p2 = 0;
        int n = nums.size();

        while (p1 < n) {
            if (nums[p1] % 2 != 0) {
                p1++;
            }
             else {
                swap(nums[p1], nums[p2]);
                p1++;
                p2++;
            }
        }
        return nums;
    }
};
