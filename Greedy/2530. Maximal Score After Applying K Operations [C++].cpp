#include <queue>
#include <cmath>
#include <vector>

class Solution {
public:
    long long maxKelements(std::vector<int>& nums, int k) {
        std::priority_queue<long long> maxHeap;
        
        for (int num : nums) {
            maxHeap.push(num);
        }
        
        long long score = 0;
        
        for (int i = 0; i < k; ++i) {
            long long maxVal = maxHeap.top();
            maxHeap.pop();
            
            score += maxVal;
            
            maxHeap.push((maxVal + 2) / 3);
        }
        
        return score;
    }
};
