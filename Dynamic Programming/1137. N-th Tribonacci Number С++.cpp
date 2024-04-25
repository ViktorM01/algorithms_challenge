class Solution {
public:
    int tribonacci(int n) {
        std::vector<int> lst = {0, 1, 1};
        if (n <= 2) {
            return lst[n];
        } else {
            while (n >= lst.size()) {
                lst.push_back(lst[lst.size() - 3] + lst[lst.size() - 2] + lst[lst.size() - 1]);
            }
            return lst[lst.size() - 1];
        }        
    }
};
