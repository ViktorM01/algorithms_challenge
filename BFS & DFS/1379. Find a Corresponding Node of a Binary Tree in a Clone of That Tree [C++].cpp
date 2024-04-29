/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <deque>
using namespace std;

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        deque<pair<TreeNode*, TreeNode*>> queue;
        queue.push_back({original, cloned});

        while (!queue.empty()) {
            auto [orig, clone] = queue.front();
            queue.pop_front();
            if (orig == target) {
                return clone;
            }
            if (orig->left) {
                queue.push_back({orig->left, clone->left});
            }
            if (orig->right) {
                queue.push_back({orig->right, clone->right});
            }
        }
        return nullptr;
    }
};
