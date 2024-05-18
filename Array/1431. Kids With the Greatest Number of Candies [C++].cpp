#include <vector>
#include <algorithm> // For std::max_element

class Solution {
public:
    std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies) {
        std::vector<bool> result;
        int max_value = *std::max_element(candies.begin(), candies.end());

        for (int candy : candies) {
            if (candy + extraCandies >= max_value) {
                result.push_back(true);
            } else {
                result.push_back(false);
            }
        }

        return result;
    }
};
