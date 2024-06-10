#include <vector>
#include <string>
#include <numeric>
#include <cmath>

class Solution {
public:
    int differenceOfSum(std::vector<int>& nums) {
        int sum_of_nums = std::accumulate(nums.begin(), nums.end(), 0);

        int digit_sum = 0;
        for (int num : nums) {
            while (num > 0) {
                digit_sum += num % 10;
                num /= 10;
            }
        }

        return std::abs(sum_of_nums - digit_sum);
    }
};
