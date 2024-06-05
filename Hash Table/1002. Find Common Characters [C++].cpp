#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<int> min_freq(26, INT_MAX);
        
        for (const string& word : words) {
            vector<int> freq(26, 0);
            for (char c : word) {
                freq[c - 'a']++;
            }
            for (int i = 0; i < 26; ++i) {
                min_freq[i] = min(min_freq[i], freq[i]);
            }
        }
        
        vector<string> result;
        for (int i = 0; i < 26; ++i) {
            for (int j = 0; j < min_freq[i]; ++j) {
                result.push_back(string(1, i + 'a'));
            }
        }
        
        return result;
    }
};
