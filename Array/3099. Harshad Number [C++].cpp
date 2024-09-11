class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        int sum_of_digits = 0, original_x = x;
        
        while (x > 0) {
            sum_of_digits += x % 10;
            x /= 10;
        }
        if (original_x % sum_of_digits == 0) {
            return sum_of_digits;
        } else {
            return -1;
        }
    }
};
