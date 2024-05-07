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
    ListNode* doubleIt(ListNode* head) {
        ListNode* reversed_list = reverseList(head);
        int carry = 0;
        ListNode* cur = reversed_list;
        ListNode* prev = nullptr;

        while (cur) {
            int new_val = cur->val * 2 + carry;
            cur->val = new_val % 10;
            carry = new_val > 9 ? 1 : 0;
            prev = cur;
            cur = cur->next;
        }

        if (carry) {
            prev->next = new ListNode(carry);
        }

        ListNode* result = reverseList(reversed_list);

        return result;
    }

private:
    ListNode* reverseList(ListNode* node) {
        ListNode* prev = nullptr;
        ListNode* cur = node;

        while (cur) {
            ListNode* next_node = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next_node;
        }

        return prev;
    }
};
