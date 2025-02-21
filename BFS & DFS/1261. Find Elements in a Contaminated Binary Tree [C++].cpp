/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <unordered_set>
using namespace std;


class FindElements {
private:
    unordered_set<int> elements;

    void recoverTree(TreeNode* node) {
        if (!node) return;
        elements.insert(node->val);
        if (node->left) {
            node->left->val = 2 * node->val + 1;
            recoverTree(node->left);
        }
        if (node->right) {
            node->right->val = 2 * node->val + 2;
            recoverTree(node->right);
        }
    }

public:
    FindElements(TreeNode* root) {
        if (root) {
            root->val = 0;
            recoverTree(root);
        }
    }

    bool find(int target) {
        return elements.find(target) != elements.end();
    }
};

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */
