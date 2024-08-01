class Solution {
public:
    int countSeniors(const std::vector<std::string>& details) {
        int count = 0;
        for (const auto& s : details) {
            int age = std::stoi(s.substr(11, 2));
            if (age > 60) {
                count++;
            }
        }
        return count;
    }
};
