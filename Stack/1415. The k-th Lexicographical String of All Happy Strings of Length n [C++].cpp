#include <queue>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string getHappyString(int n, int k) {
        queue<string> charQueue;
        charQueue.push("a");
        charQueue.push("b");
        charQueue.push("c");
        
        vector<string> ansList;
        
        while (!charQueue.empty()) {
            string s = charQueue.front();
            charQueue.pop();
            
            if (s.length() == n) {
                ansList.push_back(s);
                continue;
            }
            
            for (char ch : {'a', 'b', 'c'}) {
                if (s.back() != ch) {
                    charQueue.push(s + ch);
                }
            }
        }
        
        if (k > ansList.size()) {
            return "";
        }
        
        return ansList[k - 1];
    }
};
