#include <string>

class Solution {
public:
    int compareVersion(std::string version1, std::string version2) {
        int f = 0, s = 0;

        while (f < version1.size() || s < version2.size()) {
            int p1 = 0, p2 = 0;

            while (f < version1.size() && version1[f] != '.') {
                p1 = p1 * 10 + (version1[f] - '0');
                f++;
            }
            while (s < version2.size() && version2[s] != '.') {
                p2 = p2 * 10 + (version2[s] - '0');
                s++;
            }

            if (p1 > p2)
                return 1;
            if (p1 < p2)
                return -1;

            f++;
            s++;
        }

        return 0;
    }
};
