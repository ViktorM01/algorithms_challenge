class Solution {
public:
    std::vector<int> pivotArray(std::vector<int>& nums, int pivot) {
        std::vector<int> lst1;
        std::vector<int> lst2;
        std::vector<int> lst3;

        for (int el : nums) {
            if (el < pivot) {
                lst1.push_back(el);
            } else if (el == pivot) {
                lst2.push_back(el);
            } else {
                lst3.push_back(el);
            }
        }

        lst1.insert(lst1.end(), lst2.begin(), lst2.end());
        lst1.insert(lst1.end(), lst3.begin(), lst3.end());

        return lst1;
    }
};
