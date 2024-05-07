# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list = self.reverse_list(head)
        carry = 0
        cur, prev = reversed_list, None

        while cur:
            new_val = cur.val * 2 + carry
            cur.val = new_val % 10
            carry = 1 if new_val > 9 else 0
            prev, cur = cur, cur.next

        if carry:
            prev.next = ListNode(carry)

        result = self.reverse_list(reversed_list)

        return result

    def reverse_list(self, node: ListNode) -> ListNode:
        prev, cur = None, node

        while cur:
            next_node = cur.next
            cur.next = prev
            prev, cur = cur, next_node

        return prev
