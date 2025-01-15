#include <iostream>
#include <bitset>
using namespace std;

class Solution {
public:
    int minimizeXor(int num1, int num2) {
        int b_num1 = __builtin_popcount(num1);
        int b_num2 = __builtin_popcount(num2);
        int ans = num1;

        for (int i = 0; i < 32; ++i) {
            if (b_num1 > b_num2 && (num1 & (1 << i))) {
                ans ^= (1 << i);
                b_num1--;
            }
            if (b_num1 < b_num2 && !(num1 & (1 << i))) {
                ans ^= (1 << i);
                b_num1++;
            }
        }

        return ans;
    }
};
