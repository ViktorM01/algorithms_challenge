class Solution {
public:
    bool checkIfPangram(const std::string& sentence) {
        std::unordered_set<char> uniqueChars(sentence.begin(), sentence.end());
        return uniqueChars.size() == 26;
    }
};
