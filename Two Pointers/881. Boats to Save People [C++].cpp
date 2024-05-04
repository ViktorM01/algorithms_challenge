#include <vector>
#include <algorithm>

class Solution {
public:
    int numRescueBoats(std::vector<int>& people, int limit) {
        std::sort(people.begin(), people.end());
        int boat = 0;
        int l = 0, r = people.size() - 1;

        while (l <= r) {
            boat++;
            if (people[l] + people[r] <= limit) {
                l++;
            }
            r--;
        }

        return boat;
    }
};
