#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<int> sort_scores = score;
        sort(sort_scores.rbegin(), sort_scores.rend());
        
        vector<string> medals = {"Gold Medal", "Silver Medal", "Bronze Medal"};

        unordered_map<int, string> rank_map;
        for (int i = 0; i < sort_scores.size(); ++i) {
            if (i < 3) {
                rank_map[sort_scores[i]] = medals[i];
            } else {
                rank_map[sort_scores[i]] = to_string(i + 1);
            }
        }

        vector<string> result;
        for (int s : score) {
            result.push_back(rank_map[s]);
        }

        return result;
    }
};
