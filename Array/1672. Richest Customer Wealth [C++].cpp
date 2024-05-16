#include <vector>

class Solution {
public:
    int maximumWealth(std::vector<std::vector<int>>& accounts) {
        int max_wealth = 0;
        for (const auto& account : accounts) {
            int current_wealth = 0;
            for (int wealth : account) {
                current_wealth += wealth;
            }
            if (current_wealth > max_wealth) {
                max_wealth = current_wealth;
            }
        }
        return max_wealth;
    }
};
