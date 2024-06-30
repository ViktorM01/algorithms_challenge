class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        int n = A.size();
        vector<int> lst(n, 0);
        unordered_set<int> sub_list;

        for (int i = 0; i < n; ++i){
            sub_list.insert(A[i]);
            sub_list.insert(B[i]);
            lst[i] = 2 * (i + 1) - sub_list.size();
        }
        return lst;
    }
};
