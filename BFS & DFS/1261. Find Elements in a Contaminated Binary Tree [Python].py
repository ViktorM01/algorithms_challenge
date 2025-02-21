# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.recover_values = set()
        root.val = 0
        self.recover_binary_tree(root)
    
    def recover_binary_tree(self, root: Optional[TreeNode]):
        if not root:
            return
        self.recover_values.add(root.val)
        if root.left:
            root.left.val = 2 * root.val + 1
            self.recover_binary_tree(root.left)
        if root.right:
            root.right.val = 2 * root.val + 2
            self.recover_binary_tree(root.right)

    def find(self, target: int) -> bool:
        return target in self.recover_values

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
