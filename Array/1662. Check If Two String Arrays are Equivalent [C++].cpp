#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string lst1, lst2;
        for (const string& w : word1) {
            lst1 += w;
        }
        for (const string& w : word2) {
            lst2 += w;
        }
        return lst1 == lst2;
    }
};
