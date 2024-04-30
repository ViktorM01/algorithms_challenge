#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    long long wonderfulSubstrings(string word) {
        vector<int> c(1024, 0);
        long long res = 0;
        int pref_xor = 0;
        c[pref_xor] = 1;

        for (char s : word) {
            int s_indx = s - 'a';
            pref_xor ^= 1 << s_indx;
            res += c[pref_xor];
            for (int i = 0; i < 10; ++i) {
                res += c[pref_xor ^ (1 << i)];
            }
            c[pref_xor]++;
        }

        return res;
    }
};
