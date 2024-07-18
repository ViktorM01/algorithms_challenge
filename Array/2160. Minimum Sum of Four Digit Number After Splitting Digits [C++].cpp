class Solution {
public:
    int minimumSum(int num) {
        std::string str_num = std::to_string(num);
        std::sort(str_num.begin(), str_num.end(), std::greater<char>());
        
        int digit1 = str_num[0] - '0';
        int digit2 = str_num[1] - '0';
        int digit3 = str_num[2] - '0';
        int digit4 = str_num[3] - '0';

        return digit1 + digit2 + (digit3 + digit4) * 10;
    }
};
