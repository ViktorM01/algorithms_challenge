# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:
        self.input_str = s
        self.pos = 0
        self.depth = 0
        dummy = TreeNode(-1)
        self._construct(dummy, 0)
        return dummy.left

    def _construct(self, parent_node, parent_depth):
        while self.pos < len(self.input_str) and self.depth == parent_depth:
            val = 0
            while self.pos < len(self.input_str) and self.input_str[self.pos].isdigit():
                val = val * 10 + int(self.input_str[self.pos])
                self.pos += 1
            
            new_node = TreeNode(val)
            
            if not parent_node.left:
                parent_node.left = new_node
            else:
                parent_node.right = new_node
            
            self.depth = 0
            while self.pos < len(self.input_str) and self.input_str[self.pos] == '-':
                self.depth += 1
                self.pos += 1
            
            self._construct(new_node, parent_depth + 1)
