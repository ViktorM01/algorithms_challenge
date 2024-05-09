#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        ios_base::sync_with_stdio(false); // Disable synchronization to improve performance
        cin.tie(nullptr); // Unlink cin from cout to improve performance
        cout.tie(nullptr);

        sort(happiness.begin(), happiness.end(), greater<int>());
        long long sum = 0;

        for (int i = 0; i < happiness.size() && k > 0; ++i, --k) {
            int adjusted = max(happiness[i] - i, 0);
            sum += adjusted;
        }

        return sum;
    }
};
