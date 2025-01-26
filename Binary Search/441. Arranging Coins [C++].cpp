class Solution {
public:
    int arrangeCoins(int n) {
        long l = 1, r = n;
        while (l <= r) {
            long mid = l + (r - l) / 2;
            long num = (mid * (mid + 1)) / 2;
            if (num <= n) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return r;
    }
};
