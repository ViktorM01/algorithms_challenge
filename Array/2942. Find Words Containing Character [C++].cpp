#include <vector>
#include <string>

class Solution {
public:
    std::vector<int> findWordsContaining(const std::vector<std::string>& words, char x) {
        std::vector<int> lst;
        
        for (int i = 0; i < words.size(); ++i) {
            if (words[i].find(x) != std::string::npos) {
                lst.push_back(i);
            }
        }
        
        return lst;
    }
};
