#include <vector>
#include <string>

class Solution {
public:
    int finalValueAfterOperations(std::vector<std::string>& operations) {
        int val = 0;

        for (const std::string& op : operations) {
            if (op == "++X" || op == "X++") {
                val += 1;
            }
        }
        
        return val - (operations.size() - val);
    }
};
