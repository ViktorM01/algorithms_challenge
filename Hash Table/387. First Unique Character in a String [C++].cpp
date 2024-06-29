class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> countMap;
        vector<int> uniqueIndexes;
        for (char ch : s) {
            countMap[ch]++;
        }
        for (const auto& pair : countMap) {
            if (pair.second == 1) {
                uniqueIndexes.push_back(s.find(pair.first));
            }
        }
        if (!uniqueIndexes.empty()) {
            return *std::min_element(uniqueIndexes.begin(), uniqueIndexes.end());
        } else {
            return -1;
        }
    }
};
