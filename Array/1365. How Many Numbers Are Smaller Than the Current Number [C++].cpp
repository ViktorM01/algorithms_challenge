#include <vector>
#include <map>
#include <algorithm>

class Solution {
public:
    std::vector<int> smallerNumbersThanCurrent(std::vector<int>& nums) {
        std::vector<int> nums_sort = nums;
        std::sort(nums_sort.begin(), nums_sort.end());

        std::map<int, int> map_dict;
        for (int i = 0; i < nums_sort.size(); ++i) {
            if (map_dict.find(nums_sort[i]) == map_dict.end()) {
                map_dict[nums_sort[i]] = i;
            }
        }

        std::vector<int> flst;
        for (int i = 0; i < nums.size(); ++i) {
            flst.push_back(map_dict[nums[i]]);
        }

        return flst;
    }
};
