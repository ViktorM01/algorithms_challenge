# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while(curr):
            if(curr.val == 0):
                s = 0
                tar = curr
                curr = curr.next
                while(curr.val != 0):
                    s += curr.val
                    curr = curr.next
                tar.val = s
                if(curr.next):
                    tar.next = curr
                else:
                    tar.next = None
                    break
        return head
