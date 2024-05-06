/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
        ListNode* cur = head;
        stack<ListNode*> stk;

        while (cur) {
            while (!stk.empty() && stk.top()->val < cur->val) {
                stk.pop();
            }
            stk.push(cur);
            cur = cur->next;
        }

        ListNode* nnt = nullptr;
        while (!stk.empty()) {
            cur = stk.top();
            stk.pop();
            cur->next = nnt;
            nnt = cur;
        }

        return cur;
    }
};
