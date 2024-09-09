class Solution {
public:
    int maxArea(vector<int>& height) {
       int l = 0, r = height.size() - 1, max_vol = 0;

       while (l < r) {
        max_vol = max((r - l) * min(height[l], height[r]), max_vol);
        if (height[l] < height[r]) {
            ++l;
        }
        else {
            --r;
            }
        }
       return max_vol;
    }
};
