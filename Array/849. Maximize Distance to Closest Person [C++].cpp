class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int res = 0, prev = -1;

        for (int i = 0; i < seats.size(); ++i) {
            if (seats[i] > 0) {
                int dist = (prev == -1) ? i : (i - prev) / 2;
                res = std::max(res, dist);
                prev = i;
            }
        }
        if (seats.back() == 0) {
            res = std::max(res, static_cast<int>(seats.size()) - 1 - prev);
        }
        return res;
    }
};
