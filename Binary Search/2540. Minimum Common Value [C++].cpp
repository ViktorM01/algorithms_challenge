class Solution {
public:
    int getCommon(std::vector<int>& nums1, std::vector<int>& nums2) {
        for (int v : nums1) {
            auto it = std::lower_bound(nums2.begin(), nums2.end(), v);
            if (it != nums2.end() && *it == v) {
                return v;
            }
        }
        return -1;
    }
};
