class Solution {
public:
    int getLucky(string s, int k) {
        string numb = "";
        for (char x : s) {
            numb += to_string(x - 'a' + 1);
        }
        while (k > 0) {
            int temp = 0;
            for (char x : numb) {
                temp += x - '0';
            }
            numb = to_string(temp);
            k--;
        }
        return stoi(numb);
    }
};
