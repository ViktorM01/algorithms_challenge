class Solution {
public:
    std::string reverseParentheses(std::string s) {
        std::stack<char> stack;
        
        for (char ch : s) {
            if (ch == ')') {
                std::string rev;
                while (!stack.empty() && stack.top() != '(') {
                    rev += stack.top();
                    stack.pop();
                }
                if (!stack.empty() && stack.top() == '(') {
                    stack.pop();
                }
                for (char c : rev) {
                    stack.push(c);
                }
            } else {
                stack.push(ch);
            }
        }
        
        std::string result;
        while (!stack.empty()) {
            result += stack.top();
            stack.pop();
        }
        std::reverse(result.begin(), result.end());
        
        return result;
    }
};
