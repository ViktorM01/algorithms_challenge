class Solution {
public:
    std::vector<std::string> findWords(std::vector<std::string>& words) {
        std::vector<std::string> result;
        std::string row1 = "qwertyuiop";
        std::string row2 = "asdfghjkl";
        std::string row3 = "zxcvbnm";
        
        for (const auto& word : words) {
            std::unordered_set<char> len_word;
            for (char ch : word) {
                len_word.insert(tolower(ch));
            }

            int c = std::max({
                countCommon(len_word, row1),
                countCommon(len_word, row2),
                countCommon(len_word, row3)
            });

            if (c == len_word.size()) {
                result.push_back(word);
            }
        }

        return result;
    }

private:
    int countCommon(const std::unordered_set<char>& set, const std::string& row) {
        int count = 0;
        for (char ch : row) {
            if (set.find(ch) != set.end()) {
                ++count;
            }
        }
        return count;
    }
};
