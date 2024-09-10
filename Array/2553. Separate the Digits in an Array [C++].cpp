class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> lst;
        for (int num : nums) {
            string numStr = to_string(num);
            for (char digit : numStr) {
                lst.push_back(digit - '0');
            }
        }
        return lst;
    }
};
