#include <vector>

class Solution {
public:
    std::vector<int> getConcatenation(std::vector<int>& nums) {
        std::vector<int> result;
        result.reserve(nums.size() * 2); // Reserve space for the concatenated vector
        
        // Copy nums vector twice to result
        result.insert(result.end(), nums.begin(), nums.end());
        result.insert(result.end(), nums.begin(), nums.end());
        
        return result;
    }
};
