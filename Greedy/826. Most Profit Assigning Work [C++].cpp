#include <vector>
#include <algorithm>
#include <utility>

class Solution {
public:
    int maxProfitAssignment(std::vector<int>& difficulty, std::vector<int>& profit, std::vector<int>& worker) {

        std::vector<std::pair<int, int>> jobs;
        for (size_t i = 0; i < difficulty.size(); ++i) {
            jobs.emplace_back(difficulty[i], profit[i]);
        }
        std::sort(jobs.begin(), jobs.end());
        
        std::sort(worker.begin(), worker.end());

        int ans = 0, j = 0, maxp = 0;
        
        for (int w : worker) {

            while (j < jobs.size() && jobs[j].first <= w) {
                maxp = std::max(maxp, jobs[j].second);
                ++j;
            }

            ans += maxp;
        }
        return ans;
    }
};
