#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool areOccurrencesEqual(string s) {
        unordered_map<char, int> hash_table;
        for(char c : s) {
            hash_table[c]++;
        }

        vector<int> counts;
        for(auto& pair : hash_table) {
            counts.push_back(pair.second);
        }

        sort(counts.begin(), counts.end());
        return adjacent_find(counts.begin(), counts.end(), not_equal_to<int>()) == counts.end();
    }
};
