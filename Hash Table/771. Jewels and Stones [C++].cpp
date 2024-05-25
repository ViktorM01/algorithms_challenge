#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <string>

class Solution {
public:
    int numJewelsInStones(std::string jewels, std::string stones) {
        std::unordered_set<char> jewelSet(jewels.begin(), jewels.end());
        std::unordered_map<char, int> stoneCount;
        for (char stone : stones) {
            if (jewelSet.find(stone) != jewelSet.end()) {
                stoneCount[stone]++;
            }
        }
        int numJewels = 0;
        for (const auto& pair : stoneCount) {
            numJewels += pair.second;
        }

        return numJewels;
    }
};
