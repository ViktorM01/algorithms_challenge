class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        vector<vector<int>> ans;
        int i = 0, j = 0, N = firstList.size(), M = secondList.size();
        while (i < N && j < M) {
            int head_1 = firstList[i][0], tail_1 = firstList[i][1];
            int head_2 = secondList[j][0], tail_2 = secondList[j][1];

            int head_max = max(head_1, head_2);
            int tail_min = min(tail_1, tail_2);

            if (head_max <= tail_min) {
                ans.push_back({head_max, tail_min});
            } 
            if (tail_1 < tail_2) {
                i++;
            } else {
                j++;
            }

        }
        return ans;
    }
};
